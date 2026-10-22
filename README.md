<div align="center">

# 🧠 Free AI Bible
### Build more. Spend less. Find your next AI stack.

**Free AI APIs, local models, coding agents and practical starters — with the catches made visible.**

[![Stars](https://img.shields.io/github/stars/abbosaliboev/free-ai-bible?style=for-the-badge&color=yellow)](https://github.com/abbosaliboev/free-ai-bible/stargazers)
[![Checks](https://github.com/abbosaliboev/free-ai-bible/actions/workflows/checks.yml/badge.svg)](https://github.com/abbosaliboev/free-ai-bible/actions/workflows/checks.yml)
[![MIT](https://img.shields.io/badge/Directory-MIT-blue)](LICENSE)

[**🔎 Search & filter the directory**](https://abbosaliboev.github.io/free-ai-bible/catalog.html) · [**⚡ Pick a stack**](#pick-your-stack) · [**🤝 Make your first contribution**](CONTRIBUTING.md)

**Save your next weekend of research. ⭐ Star this repo to find it when you need it.**

English · [العربية](translations/README.ar.md) · [中文](translations/README.zh-CN.md) · [한국어](translations/README.ko.md) · [Español](translations/README.es.md) · [Русский](translations/README.ru.md) · [日本語](translations/README.ja.md) · [O‘zbek](translations/README.uz.md)

</div>

## Pick your stack

| I want to… | Start here | What to know |
|---|---|---|
| Build a cloud chatbot | [Groq starter](templates/chatbot-groq/) · [API picker](comparison-charts/which-llm-api.md) | Account required; requests and tokens have separate limits |
| Chat offline | [Ollama setup](scripts/setup-ollama.sh) | Download a local model first; RAM and electricity matter |
| Search my documents | [Local RAG starter](templates/rag-pipeline-free/) | Ollama + local embeddings + Chroma |
| Generate images | [Image API starter](templates/image-gen-api/) · [Image picker](comparison-charts/image-gen-picker.md) | First run downloads weights; GPU helps |
| Build a voice assistant | [Voice starter](templates/voice-assistant/) | Local speech recognition and TTS; text goes to Groq |
| Code with local models | Continue or Aider in the catalog below | Free assistant software does not make a paid model API free |
| Work in Arabic | [Arabic guide](translations/README.ar.md) | Qwen3 for text; Qwen3-ASR for speech; test your dialect |

## What changed

**October 22, 2026:** added 24 resources, including Qwen3, Qwen3-ASR/TTS, EmbeddingGemma, Docling, local coding tools and agent frameworks. Added Arabic, a searchable directory, JSON/CSV exports and clearer review labels. [Changelog](CHANGELOG.md).

**Important correction:** Hugging Face Inference Providers currently lists **no monthly credits for free accounts**. Groq quotas are model-specific, and Cloudflare's free compute allocation excludes some models. Check the linked official sources before building around a quota.

## Read the labels before choosing

- **Free tier:** recurring hosted allowance, with account, region and usage restrictions.
- **Local:** downloadable software or weights. Your hardware, electricity, hosting and model licenses still matter. Optional cloud integrations may charge.
- **Needs review:** preserved from the earlier directory; the old free quota has been removed until someone checks current terms.
- **Paid:** a previously listed free option whose current terms no longer qualify; retained to explain the change.

**Docs reviewed** means an official documentation or project page was reviewed on the recorded date. It does **not** mean signup, billing, performance or every model was tested. Card requirements marked “unknown” need account-level confirmation. [Review policy](docs/VERIFICATION.md).

## Directory

Search by task, category, cost type and card requirement on the [directory page](https://abbosaliboev.github.io/free-ai-bible/catalog.html). Bookmark a filtered URL, save favorites on your device, or download [JSON](data/resources.json) / [CSV](data/resources.csv).

<!-- CATALOG:START -->
**72 resources · 34 docs reviewed · 38 awaiting review.** Counts are generated from the catalog.

### LLM APIs

| Resource | Access | Useful for / limitations | Source checked |
|---|---|---|---|
| [Groq](https://console.groq.com) | free-tier · card: no | Hosted LLM and speech APIs; gpt-oss models are listed in the current free plan. Model-specific request AND token limits; read the console before sizing a workload. | [Official source](https://console.groq.com/docs/rate-limits) · 2026-10-22 |
| [Google AI Studio](https://aistudio.google.com) | free-tier · card: no | Gemini text and multimodal prototyping on eligible free-tier models. Model, region and project quotas vary. Free-tier content may improve Google products. | [Official source](https://ai.google.dev/gemini-api/docs/pricing) · 2026-10-22 |
| [Mistral AI](https://mistral.ai) | free-tier · card: unknown | Mistral Studio Free access for experimentation; inspect available models in your account. Account and model limits apply; free access is not a production capacity promise. | [Official source](https://mistral.ai/pricing/) · 2026-10-22 |
| [Cerebras](https://cerebras.ai) | free-tier · card: unknown | Hosted inference with a documented free tier. Lower free-tier rate limits; consult current model and context availability. | [Official source](https://inference-docs.cerebras.ai/support/pricing) · 2026-10-22 |
| [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai) | free-tier · card: conditional | Edge inference with a daily free compute allocation on supported models. 10,000 neurons/day; some models require a paid plan or prepaid credits. | [Official source](https://developers.cloudflare.com/workers-ai/platform/pricing/) · 2026-10-22 |
| [Hugging Face Inference](https://huggingface.co/inference-api) | paid · card: conditional | Inference Providers no longer includes monthly credits for free accounts. Free users must buy credits or upgrade; kept here to prevent outdated recommendations. | [Official source](https://huggingface.co/docs/inference-providers/pricing) · 2026-10-22 |
| [OpenRouter](https://openrouter.ai) | free-tier · card: no | One API for rotating free models; useful for comparing providers. Free plan: 50 requests/day. Model availability and upstream limits vary. | [Official source](https://openrouter.ai/pricing/) · 2026-10-22 |

### Local tools

| Resource | Access | Useful for / limitations | Source checked |
|---|---|---|---|
| [Ollama](https://ollama.com) | local · card: no | Run supported models locally; choose local model tags for offline use. Hardware, storage and model licenses apply; cloud offerings are separate. | [Official source](https://github.com/ollama/ollama) · 2026-10-22 |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | local · card: no | Build local image and video workflows with a node editor. Hardware, storage and model licenses apply; cloud offerings are separate. | [Official source](https://github.com/Comfy-Org/ComfyUI) · 2026-10-22 |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | local · card: no | Run GGUF models with CPU and supported GPU backends. Software is free to self-host; hardware, hosting and model/API costs may apply. | [Official source](https://github.com/ggml-org/llama.cpp) · 2026-10-22 |
| [MLX LM](https://github.com/ml-explore/mlx-lm) | local · card: no | Local inference and fine-tuning on Apple silicon. Requires compatible Apple hardware and sufficient memory. | [Official source](https://github.com/ml-explore/mlx-lm) · 2026-10-22 |
| [Unsloth](https://github.com/unslothai/unsloth) | local · card: no | Tools for running and fine-tuning supported open models. Hardware requirements and licenses vary by model. | [Official source](https://github.com/unslothai/unsloth) · 2026-10-22 |

### Open models

| Resource | Access | Useful for / limitations | Source checked |
|---|---|---|---|
| [Qwen3](https://github.com/QwenLM/Qwen3) | local · card: no | Open-weight multilingual reasoning models; includes Arabic and regional dialects. Apache-2.0 Qwen3 releases; choose a size your hardware supports. | [Official source](https://github.com/QwenLM/Qwen3) · 2026-10-22 |
| [EmbeddingGemma](https://deepmind.google/models/gemma/embeddinggemma/) | local · card: no | Compact multilingual embedding model for on-device retrieval. Gemma terms and model download conditions apply; local compute required. | [Official source](https://deepmind.google/models/gemma/embeddinggemma/) · 2026-10-22 |

### Coding assistants

| Resource | Access | Useful for / limitations | Source checked |
|---|---|---|---|
| [Aider](https://aider.chat/docs/faq.html) | local · card: no | Terminal coding assistant that works with your Git repository. Assistant software is open source; chosen local models or API providers have their own costs. | [Official source](https://aider.chat/docs/faq.html) · 2026-10-22 |
| [Continue](https://github.com/continuedev/continue) | local · card: no | Open-source coding agent with configurable model providers. Use local inference for local-only operation; hosted plans and API calls are separate. | [Official source](https://github.com/continuedev/continue) · 2026-10-22 |

### Image & video

| Resource | Access | Useful for / limitations | Source checked |
|---|---|---|---|
| [FLUX.1 schnell](https://github.com/black-forest-labs/flux/blob/main/README.md) | local · card: no | Downloadable text-to-image model for local workflows. The schnell variant uses Apache-2.0; other FLUX variants have different licenses. | [Official source](https://github.com/black-forest-labs/flux/blob/main/README.md) · 2026-10-22 |

### Hosting

| Resource | Access | Useful for / limitations | Source checked |
|---|---|---|---|
| [vLLM](https://github.com/vllm-project/vllm) | local · card: no | Self-host an inference server for supported models. GPU/server costs and model compatibility apply. | [Official source](https://github.com/vllm-project/vllm) · 2026-10-22 |

### Embeddings & RAG

| Resource | Access | Useful for / limitations | Source checked |
|---|---|---|---|
| [Chroma (local)](https://trychroma.com) | local · card: no | Local vector storage for document search and RAG. Hardware, storage and model licenses apply; cloud offerings are separate. | [Official source](https://github.com/chroma-core/chroma) · 2026-10-22 |
| [Docling](https://github.com/docling-project/docling) | local · card: no | Convert documents into structured data for retrieval pipelines. Software is free to self-host; hardware, hosting and model/API costs may apply. | [Official source](https://github.com/docling-project/docling) · 2026-10-22 |
| [MarkItDown](https://github.com/microsoft/markitdown) | local · card: no | Convert office documents and other files into Markdown. Optional AI integrations may call paid services; inspect configuration. | [Official source](https://github.com/microsoft/markitdown) · 2026-10-22 |
| [Qdrant (local)](https://github.com/qdrant/qdrant) | local · card: no | Self-host vector search for semantic retrieval. Software is free to self-host; hardware, hosting and model/API costs may apply. | [Official source](https://github.com/qdrant/qdrant) · 2026-10-22 |
| [pgvector](https://github.com/pgvector/pgvector) | local · card: no | Add vector similarity search to your own Postgres database. Software is free to self-host; hardware, hosting and model/API costs may apply. | [Official source](https://github.com/pgvector/pgvector) · 2026-10-22 |
| [Sentence Transformers](https://github.com/huggingface/sentence-transformers) | local · card: no | Local embeddings and reranking with a choice of model families. Each downloaded model has its own license and hardware requirements. | [Official source](https://github.com/huggingface/sentence-transformers) · 2026-10-22 |
| [RAGFlow](https://github.com/infiniflow/ragflow) | local · card: no | Self-host document retrieval and agent workflows. Requires substantial local/server resources; selected inference providers may charge. | [Official source](https://github.com/infiniflow/ragflow) · 2026-10-22 |
| [Qdrant Cloud](https://qdrant.tech/pricing/) | free-tier · card: unknown | Managed vector database with a free cluster option. Free tier: 1 GB RAM and 4 GB disk; check current eligibility and region. | [Official source](https://qdrant.tech/pricing/) · 2026-10-22 |

### Speech & audio

| Resource | Access | Useful for / limitations | Source checked |
|---|---|---|---|
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | local · card: no | Local speech recognition in C/C++ with multiple hardware backends. Software is free to self-host; hardware, hosting and model/API costs may apply. | [Official source](https://github.com/ggml-org/whisper.cpp) · 2026-10-22 |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | local · card: no | Local Whisper inference using CTranslate2. Software is free to self-host; hardware, hosting and model/API costs may apply. | [Official source](https://github.com/SYSTRAN/faster-whisper) · 2026-10-22 |
| [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) | local · card: no | Multilingual speech recognition with language detection. Check supported languages and hardware in the model card. | [Official source](https://github.com/QwenLM/Qwen3-ASR) · 2026-10-22 |
| [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | local · card: no | Downloadable speech generation and voice design models. Language coverage differs from Qwen3-ASR; use voices with permission. | [Official source](https://github.com/QwenLM/Qwen3-TTS) · 2026-10-22 |

### Agents & workflows

| Resource | Access | Useful for / limitations | Source checked |
|---|---|---|---|
| [LiteLLM](https://github.com/BerriAI/litellm) | local · card: no | A common interface and gateway for multiple model providers. Self-hosted core and enterprise features differ; upstream inference may cost money. | [Official source](https://github.com/BerriAI/litellm) · 2026-10-22 |
| [Flowise](https://github.com/FlowiseAI/Flowise) | local · card: no | Visual builder for AI workflows and agents. Self-hosted core is separate from cloud and enterprise plans; model calls may cost money. | [Official source](https://github.com/FlowiseAI/Flowise) · 2026-10-22 |
| [Dify](https://github.com/langgenius/dify) | local · card: no | Build self-hosted workflows, agents and retrieval applications. Dify license has additional conditions; cloud and model costs are separate. | [Official source](https://github.com/langgenius/dify) · 2026-10-22 |
| [smolagents](https://github.com/huggingface/smolagents) | local · card: no | A lightweight framework for building model-powered agents. Model inference is separate; run generated code in an appropriate sandbox. | [Official source](https://github.com/huggingface/smolagents) · 2026-10-22 |

<details>
<summary>Earlier entries awaiting a fresh review</summary>

These are candidates, not confirmed free recommendations. Help check one against its current official terms.

| Resource | Category | Status |
|---|---|---|
| [Cohere](https://cohere.com) | LLM APIs | Needs review |
| [Together AI](https://together.ai) | LLM APIs | Needs review |
| [Novita AI](https://novita.ai) | LLM APIs | Needs review |
| [Stable Diffusion (Local)](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | Image & video | Needs review |
| [Leonardo.ai](https://leonardo.ai) | Image & video | Needs review |
| [Adobe Firefly](https://firefly.adobe.com) | Image & video | Needs review |
| [Ideogram](https://ideogram.ai) | Image & video | Needs review |
| [Flux (via Replicate)](https://replicate.com) | Image & video | Needs review |
| [Kling AI](https://klingai.com) | Image & video | Needs review |
| [Hailuo AI](https://hailuoai.com) | Image & video | Needs review |
| [Craiyon](https://www.craiyon.com) | Image & video | Needs review |
| [Pika Labs](https://pika.art) | Image & video | Needs review |
| [Hugging Face Spaces](https://huggingface.co/spaces) | Hosting | Needs review |
| [Google Colab](https://colab.research.google.com) | Hosting | Needs review |
| [Modal](https://modal.com) | Hosting | Needs review |
| [Vercel](https://vercel.com) | Hosting | Needs review |
| [Railway](https://railway.app) | Hosting | Needs review |
| [Render](https://render.com) | Hosting | Needs review |
| [Replicate](https://replicate.com) | Hosting | Needs review |
| [Cloudflare Workers](https://workers.cloudflare.com) | Hosting | Needs review |
| [Kaggle Notebooks](https://kaggle.com) | Hosting | Needs review |
| [LM Studio](https://lmstudio.ai) | Local tools | Needs review |
| [Whisper (local)](https://github.com/openai/whisper) | Local tools | Needs review |
| [Anything LLM](https://anythingllm.com) | Local tools | Needs review |
| [LocalAI](https://localai.io) | Local tools | Needs review |
| [Jan.ai](https://jan.ai) | Local tools | Needs review |
| [Open WebUI](https://github.com/open-webui/open-webui) | Local tools | Needs review |
| [Supabase pgvector](https://supabase.com) | Embeddings & RAG | Needs review |
| [Pinecone](https://pinecone.io) | Embeddings & RAG | Needs review |
| [Weaviate Cloud](https://weaviate.io) | Embeddings & RAG | Needs review |
| [Cohere Embed](https://cohere.com) | Embeddings & RAG | Needs review |
| [Nomic Embed](https://nomic.ai) | Embeddings & RAG | Needs review |
| [Deepgram](https://deepgram.com) | Speech & audio | Needs review |
| [ElevenLabs](https://elevenlabs.io) | Speech & audio | Needs review |
| [Whisper (OpenAI)](https://openai.com/research/whisper) | Speech & audio | Needs review |
| [Suno](https://suno.com) | Speech & audio | Needs review |
| [Udio](https://udio.com) | Speech & audio | Needs review |
| [AssemblyAI](https://assemblyai.com) | Speech & audio | Needs review |

</details>
<!-- CATALOG:END -->

## Run your first local model

Install [Ollama for your OS](https://ollama.com/download), then:

```bash
ollama pull qwen3:4b
ollama run qwen3:4b
```

Pick a smaller or quantized model if memory is limited. After the download, local model inference can run offline. Cloud-tagged models require a network connection.

For the Python starters, create a virtual environment in the chosen template folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows use `.venv\Scripts\activate`. Each starter has its own setup instructions; these are learning examples, not production deployments.

## Help one developer. Improve one entry.

You do not need to build a new feature to contribute. Check one provider's free tier, test one starter, or improve one translation. [Start with a small task](docs/GOOD_FIRST_ISSUES.md).

- [Add a resource](https://github.com/abbosaliboev/free-ai-bible/issues/new?template=add-resource.yml)
- [Report a changed limit](https://github.com/abbosaliboev/free-ai-bible/issues/new?template=outdated-resource.yml)
- [Help with a translation](https://github.com/abbosaliboev/free-ai-bible/issues/new?template=translation.yml)
- [Contribution guide](CONTRIBUTING.md) · [Contributors](https://github.com/abbosaliboev/free-ai-bible/graphs/contributors)

All contributors are credited through Git history and the contributors page. No affiliate links or paid placement. Directory content uses the [MIT license](LICENSE); each listed service and model has its own terms.

## Share a useful discovery

Found a tool that saved you time? Share that specific entry or starter with your community. [Ready-to-adapt English, Arabic and Uzbek posts](docs/SHARING.md) are included. Maintainers can use the [growth checklist](docs/MAINTAINER_GUIDE.md) to track real usage and contributions.

**⭐ Keep this toolbox within reach. Star it, try a starter, and bring back one useful correction.**
