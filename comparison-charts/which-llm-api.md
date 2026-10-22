# Pick an LLM API without guessing the quota

| Need | Shortlist | Check before choosing |
|---|---|---|
| Streaming chatbot | Groq | Model availability, daily requests AND token limits |
| Text + vision | Gemini via Google AI Studio | Which models have free access, region, data-use terms |
| Compare free models | OpenRouter | Daily free allowance, provider privacy and model rotation |
| Edge application | Cloudflare Workers AI | Neuron allocation; some models require payment |
| Experiment with Mistral | Mistral Studio | Account-specific free-model access and quotas |
| No cloud inference | Ollama + a downloaded local model | RAM, model license, offline configuration |

Use [the catalog](../README.md#directory) for dated official sources, or [filter LLM APIs](https://abbosaliboev.github.io/free-ai-bible/catalog.html?category=llm&reviewed=1).

No universal “fastest” or “best” ranking is claimed. Benchmark your own prompt, output length, concurrency and language. Free tiers are useful for experiments; production capacity and support need separate planning.

Hugging Face Inference Providers currently requires purchased credits or a subscription for free-account users. Downloading open models from the Hub is a different service.
