"""Focused regressions: input-as-data, generated views and inference limits."""
import ast
import importlib.util
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

class SafetyRegressions(unittest.TestCase):
    def test_image_prompt_is_data(self):
        source = (ROOT/'scripts/setup-stable-diffusion.sh').read_text()
        python_code = source.split("python3 - <<'EOF'\n",1)[1].split('\nEOF',1)[0]
        with tempfile.TemporaryDirectory() as directory:
            stub = Path(directory)/'diffusers.py'
            stub.write_text('''import os
class Image:
 def save(self, name): pass
class StableDiffusionPipeline:
 @classmethod
 def from_pretrained(cls,*args,**kwargs): return cls()
 def __call__(self,prompt):
  assert prompt == os.environ['AI_IMAGE_PROMPT']
  return type('Result',(),{'images':[Image()]})()
''')
            (Path(directory)/'torch.py').write_text('float32 = object()\n')
            env = {**os.environ, 'PYTHONPATH':directory, 'AI_IMAGE_PROMPT':'a "quoted" city\n"); raise RuntimeError("injected") #'}
            result = subprocess.run([os.sys.executable,'-c',python_code],env=env,cwd=directory,capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)

    @unittest.skipUnless(importlib.util.find_spec('pydantic'),'Pydantic installed in CI')
    def test_image_request_bounds(self):
        from pydantic import BaseModel, Field, ValidationError
        tree = ast.parse((ROOT/'templates/image-gen-api/app.py').read_text())
        request = next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='GenerateRequest')
        namespace = {'BaseModel':BaseModel,'Field':Field,'__name__':__name__}
        exec(compile(ast.Module(body=[request],type_ignores=[]),'<request>','exec'),namespace)
        model = namespace['GenerateRequest']
        self.assertEqual(model(prompt='test').width,512)
        for data in ({'prompt':''},{'prompt':'x','width':513},{'prompt':'x','height':100000},{'prompt':'x','steps':0},{'prompt':'x','steps':51}):
            with self.subTest(data=data), self.assertRaises(ValidationError): model(**data)

    def test_voice_leaves_no_temp_file(self):
        tree = ast.parse((ROOT/'templates/voice-assistant/app.py').read_text())
        func = next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='transcribe')
        class STT:
            def transcribe(self,audio):
                self.received=audio
                return {'text':'  transcript  '}
        stt=STT(); namespace={'stt_model':stt,'np':type('NP',(),{'ndarray':object})}
        exec(compile(ast.Module(body=[func],type_ignores=[]),'<transcribe>','exec'),namespace)
        waveform=object()
        self.assertEqual(namespace['transcribe'](waveform),'transcript')
        self.assertIs(stt.received,waveform)

if __name__ == '__main__': unittest.main()
