#!/usr/bin/env python3
"""Offline catalog, generated-view, syntax and relative-link checks."""
import ast
from datetime import date
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

def check_catalog(rows):
    ids = set()
    categories = {'llm','local','models','coding','image','hosting','rag','audio','agents'}
    for r in rows:
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', r['id']), r['id']
        assert r['id'] not in ids, f"Duplicate id: {r['id']}"
        ids.add(r['id'])
        for key in ('name','summary','limits','source','url'):
            assert isinstance(r[key],str) and r[key].strip(), (r['id'],key)
        assert r['category'] in categories, r['id']
        assert r['kind'] in {'local','free-tier','trial','credit','paid','unconfirmed'}, r['id']
        assert r['card'] in {'no','yes','conditional','unknown'}, r['id']
        assert isinstance(r['tags'],list) and all(isinstance(t,str) for t in r['tags']), r['id']
        for key in ('source','url'):
            parts = urlsplit(r[key]); assert parts.scheme == 'https' and parts.netloc and not parts.username, r['id']
        assert r['verification'] in {'docs-reviewed','needs-review'}, r['id']
        if r['verification'] == 'docs-reviewed':
            assert r['reviewed'] and date.fromisoformat(r['reviewed']) <= date.today(), r['id']
        else:
            assert r['reviewed'] is None, r['id']

def main():
    check_catalog(json.loads((ROOT/'data/resources.json').read_text()))
    subprocess.run([sys.executable,str(ROOT/'scripts/build-directory.py'),'--check'],check=True)
    for folder in ('templates','scripts','tests'):
        for p in (ROOT/folder).rglob('*.py'):
            ast.parse(p.read_text(),filename=str(p))
    for p in (ROOT/'scripts').glob('*.sh'):
        subprocess.run(['bash','-n',str(p)],check=True)
    for p in ROOT.rglob('*.md'):
        if any(part in {'.git','.venv','_site'} for part in p.parts): continue
        for target in re.findall(r'\]\(([^)\s]+)\)',p.read_text()):
            parts = urlsplit(target)
            if parts.scheme or not parts.path: continue
            dest = ROOT / unquote(parts.path.lstrip('/')) if parts.path.startswith('/') else p.parent / unquote(parts.path)
            assert dest.exists(), f'Broken relative link: {p.relative_to(ROOT)} -> {target}'
    if importlib.util.find_spec('yaml'):
        import yaml
        for p in (ROOT/'.github').rglob('*.yml'):
            yaml.safe_load(p.read_text())
        yaml.safe_load((ROOT/'_config.yml').read_text())
    else:
        subprocess.run(['ruby', '-e', 'require "yaml"; ARGV.each { |f| YAML.load_file(f) }', *map(str, (ROOT/'.github').rglob('*.yml')), str(ROOT/'_config.yml')], check=True)
        print('YAML parsed using Ruby; CI uses PyYAML.')
    print('Catalog, generated files, relative links, Python and shell syntax passed.')

if __name__ == '__main__':
    main()
