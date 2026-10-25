# Free Voice Assistant

Full voice assistant pipeline: **speak → transcribe → LLM → speak back.**
Local speech recognition and speech output, with Groq free-tier text inference.

| Component | Tool | Cost |
|-----------|------|------|
| Speech-to-Text | OpenAI Whisper (local) | $0 |
| LLM | Groq configurable LLM | $0 within model-specific free limits |
| Text-to-Speech | pyttsx3 (local) | $0 |

## Setup

```bash
# macOS
brew install ffmpeg portaudio

# Linux
sudo apt install ffmpeg portaudio19-dev

pip install -r requirements.txt
export GROQ_API_KEY=your_key_here   # free at console.groq.com
python app.py
```

## Notes

- Whisper `base` model works well and is small. Swap for `medium` or `large` for better accuracy.
- First run downloads the Whisper model (~150MB, one-time).
- Speaks back using your OS's built-in TTS voices via pyttsx3.

Default LLM: `openai/gpt-oss-20b`; override with `GROQ_MODEL`. Transcripts are sent to Groq. Audio is transcribed from memory and is not written to temporary WAV files. Free-tier availability and quotas can change. Hardware, microphone permissions and OS speech dependencies apply.
