# Local or cloud AI?

| Factor | Local inference | Cloud API |
|---|---|---|
| Cost | Hardware, power, storage and maintenance | Free quotas or usage-based billing |
| Data | Can stay on your device with local configuration | Sent to a provider; read its data policy |
| Setup | Install runner and download compatible weights | Create account, configure key and select model |
| Limits | Memory, speed, concurrency and model license | Requests, tokens, account, region and terms |
| Offline | Possible after downloads | Usually requires connectivity |
| Quality | Depends on model, quantization and task | Depends on provider, model and task |

Choose local operation when offline access and control of data matter. Check telemetry, tools and integrations too: a local UI can still call cloud services.

Choose cloud APIs when you prefer managed infrastructure or lack compatible hardware. Measure latency and quality using your own workload.

A hybrid app can route tasks between both, but fallback must preserve user expectations about data handling. Do not silently send private local documents to a cloud API.

[Local RAG starter](../templates/rag-pipeline-free/) · [API picker](which-llm-api.md)
