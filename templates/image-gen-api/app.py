"""
Free image generation REST API — Stable Diffusion via diffusers.
Wraps local image generation in a simple HTTP API (FastAPI).

No API keys. No cloud. Unlimited generations.
"""

import io
import base64
from fastapi import FastAPI
from pydantic import BaseModel, Field
from threading import Lock
import torch
from diffusers import StableDiffusionPipeline

app = FastAPI(title="Free Image Generation API")
generation_lock = Lock()

print("⏳ Loading Stable Diffusion model (one-time, ~4GB download)...")
pipe = StableDiffusionPipeline.from_pretrained(
    "stable-diffusion-v1-5/stable-diffusion-v1-5",
    torch_dtype=torch.float32,
)
# Use GPU if available
if torch.cuda.is_available():
    pipe = pipe.to("cuda")
    print("✅ Running on GPU")
else:
    print("✅ Running on CPU (slower but works)")


class GenerateRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=2000)
    negative_prompt: str = Field(default="blurry, low quality, distorted", max_length=2000)
    width: int = Field(default=512, ge=64, le=768, multiple_of=8)
    height: int = Field(default=512, ge=64, le=768, multiple_of=8)
    steps: int = Field(default=20, ge=1, le=50)


class GenerateResponse(BaseModel):
    image_base64: str
    prompt: str


@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    # Serialize access to the shared pipeline to avoid concurrent GPU allocations.
    with generation_lock:
        image = pipe(
            prompt=req.prompt,
            negative_prompt=req.negative_prompt,
            width=req.width,
            height=req.height,
            num_inference_steps=req.steps,
        ).images[0]

    buf = io.BytesIO()
    image.save(buf, format="PNG")
    encoded = base64.b64encode(buf.getvalue()).decode("utf-8")

    return GenerateResponse(image_base64=encoded, prompt=req.prompt)


@app.get("/health")
def health():
    return {"status": "ok", "gpu": torch.cuda.is_available()}
