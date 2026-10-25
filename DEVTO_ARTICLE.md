---
title: Your next AI side project might need fewer subscriptions
tags: ai, opensource, webdev, programming
published: false
---

# Your next AI side project might need fewer subscriptions

Finding a free AI API is easy. Finding out what “free” actually means takes longer.

Does it reset monthly? Is it a one-time credit? Does the model need a paid account even though the platform has a free tier? And will the local tool quietly call a paid API?

I'm building [Free AI Bible](https://github.com/abbosaliboev/free-ai-bible) to make those questions easier to answer.

## A toolbox you can search

The [directory](https://abbosaliboev.github.io/free-ai-bible/catalog.html) lets you filter APIs, local models, coding assistants and retrieval tools by category, access type and card requirements. Save favorites on your device, share a filtered URL or download the JSON/CSV.

Official documentation reviews have dates. Older entries that need a fresh check are labelled. Reading pricing documentation is different from testing an account; the directory says which it does.

One example of why this matters: Hugging Face Inference Providers now lists no monthly credits for free accounts in its [official pricing documentation](https://huggingface.co/docs/inference-providers/pricing). Downloading models for local use is a different option.

## Four ways to start building

- A streaming chatbot with Groq, with the model configurable through an environment variable.
- A local RAG example using Ollama, a dedicated embedding model and Chroma.
- A Stable Diffusion REST wrapper with bounded inputs.
- A voice assistant with local speech processing and cloud text inference.

These are small learning examples. Hardware, licenses, model availability and free quotas still apply.

## Try a local model

Install [Ollama](https://ollama.com/download), then choose a model that fits your hardware:

```bash
ollama pull qwen3:4b
ollama run qwen3:4b
```

The catalog also includes tools such as Docling, Continue, Aider, whisper.cpp and multilingual model families. Arabic joins the translated guides; native-speaker review is welcome.

## Help with one useful correction

You do not need to build a big feature. Check one service's current terms, test one starter on your OS, or improve one translation. The repo includes issue forms and small suggested tasks.

[Explore the repo](https://github.com/abbosaliboev/free-ai-bible). ⭐ Star it to keep it within reach for your next build.

Which free-tier limitation surprised you recently? A link to the official change can help everyone avoid the same mistake.
