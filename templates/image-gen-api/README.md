# Free Image Generation REST API

Stable Diffusion wrapped in a FastAPI server. Unlimited generations. No API keys.

## Setup

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Usage

```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "a futuristic city at sunset, cinematic"}' \
  | python3 -c "import sys,json,base64; d=json.load(sys.stdin); open('out.png','wb').write(base64.b64decode(d['image_base64']))"

open out.png
```

## API Docs

Visit `http://localhost:8000/docs` for interactive Swagger UI.

## Notes

- First run downloads the model (~4GB, one-time only)
- GPU recommended — CPU works but is ~10x slower
- Swap `stable-diffusion-v1-5/stable-diffusion-v1-5` for a compatible StableDiffusionPipeline model (other architectures need their own pipeline)

Requests require a nonempty prompt of at most 2,000 characters, dimensions between 64 and 768 divisible by 8, and 1–50 steps. Generation is serialized per process because the pipeline is shared. This protects the demo from concurrent inference allocations; it is not a production queue or request-rate limiter. Keep the default loopback binding for local use.
