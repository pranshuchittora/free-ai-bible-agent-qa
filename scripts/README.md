# Setup helpers

Read a script before running it. Use a Python virtual environment for Python dependencies. Linux Ollama installation uses the upstream installer; macOS uses Homebrew or directs you to the official app.

| Script | Purpose |
|---|---|
| `setup-groq.sh` | Install Groq SDK and test a key; input is hidden and the script never saves it to a shell profile |
| `setup-ollama.sh` | Install/start Ollama, pull a local model and chat; override with `OLLAMA_MODEL` |
| `setup-stable-diffusion.sh` | Install image dependencies, download weights and create `output.png` |
| `build-directory.py` | Generate README catalog tables, CSV and browser data |
| `check-repo.py` | Check catalog integrity, generated files, local links and Python/shell syntax |
| `check-links.py` | Check catalog source URLs; availability only, not free-tier verification |

```bash
python3 -m venv .venv
source .venv/bin/activate
bash scripts/setup-groq.sh
```

Scripts install software and download models on request. Download time, compatibility, storage and memory vary. They are not executed by repository checks.
