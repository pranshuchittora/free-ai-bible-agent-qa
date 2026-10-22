#!/usr/bin/env python3
"""Generate tracked catalog views from data/resources.json. Use --check in CI."""
import argparse
import csv
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {'llm': 'LLM APIs', 'local': 'Local tools', 'models': 'Open models', 'coding': 'Coding assistants', 'image': 'Image & video', 'hosting': 'Hosting', 'rag': 'Embeddings & RAG', 'audio': 'Speech & audio', 'agents': 'Agents & workflows'}

def render():
    rows = json.loads((ROOT / 'data/resources.json').read_text())
    reviewed = [r for r in rows if r['verification'] == 'docs-reviewed']
    sections = {
        'llm': ('llm-apis', '🔥 Free LLM APIs'),
        'image': ('image-tools', '🎨 Image Generation'),
        'local': ('local-tools', '🖥️ Run AI on Your Own Machine'),
        'coding': ('coding-tools', '💻 AI Coding Assistants'),
        'models': ('open-models', '🧠 Open Models to Explore'),
        'rag': ('rag-tools', '📦 Embeddings, Documents & RAG'),
        'audio': ('audio-tools', '🎙️ Speech, Audio & Transcription'),
        'agents': ('agent-tools', '🤖 Build Agents & Workflows'),
        'hosting': ('hosting-tools', '🚀 Model Serving & Hosting'),
    }
    short = {
        'Groq': ('Streaming chat & speech APIs', 'Model-specific free limits'),
        'Google AI Studio': ('Gemini text, vision & prototyping', 'Free on eligible models'),
        'Mistral AI': ('Experiment with Mistral models', 'Free plan; account limits apply'),
        'Cerebras': ('Hosted LLM inference', 'Free tier with lower limits'),
        'Cloudflare Workers AI': ('Run inference at the edge', '10,000 neurons/day on eligible models'),
        'OpenRouter': ('Try models through one API', '50 free-plan requests/day'),
        'Ollama': ('Download a model and start chatting', 'Local'),
        'ComfyUI': ('Build image & video workflows visually', 'Local'),
        'llama.cpp': ('Run GGUF models on CPU or GPU', 'Local'),
        'MLX LM': ('Run & fine-tune models on Apple silicon', 'Local · compatible Mac required'),
        'Unsloth': ('Run & fine-tune supported models', 'Local · hardware varies'),
        'Aider': ('Pair-program from your terminal', 'Free software; bring a model'),
        'Continue': ('Code with a configurable AI agent', 'Free software; bring a model'),
        'Qwen3': ('Multilingual chat & reasoning, including Arabic', 'Local · Apache-2.0 releases'),
        'EmbeddingGemma': ('Compact multilingual embeddings', 'Local · Gemma terms'),
        'FLUX.1 schnell': ('Generate images with downloadable weights', 'Local · Apache-2.0 variant'),
        'Chroma (local)': ('Store & search document embeddings', 'Local'),
        'Docling': ('Turn documents into AI-ready data', 'Local'),
        'MarkItDown': ('Convert files to Markdown', 'Local · optional API integrations'),
        'Qdrant (local)': ('Self-host vector search', 'Local'),
        'pgvector': ('Add vector search to Postgres', 'Local'),
        'Sentence Transformers': ('Generate embeddings & rerank results', 'Local · choose a model'),
        'RAGFlow': ('Build document retrieval workflows', 'Self-hosted · needs server resources'),
        'Qdrant Cloud': ('Managed vector search', 'Free cluster: 1 GB RAM / 4 GB disk'),
        'whisper.cpp': ('Transcribe speech with a C/C++ runtime', 'Local'),
        'faster-whisper': ('Run Whisper with CTranslate2', 'Local'),
        'Qwen3-ASR': ('Recognize multilingual speech, including Arabic', 'Local'),
        'Qwen3-TTS': ('Generate speech & design voices', 'Local · check language support'),
        'LiteLLM': ('Connect model providers through one gateway', 'Self-hosted core; model calls separate'),
        'Flowise': ('Build AI workflows with a visual editor', 'Self-hosted core; model calls separate'),
        'Dify': ('Create agents & RAG applications', 'Self-hosted · Dify license applies'),
        'smolagents': ('Build lightweight model-powered agents', 'Free framework; bring a model'),
        'vLLM': ('Serve supported LLMs yourself', 'Free software; server costs apply'),
    }
    lines = [f'**{len(rows)} resources to explore.** Search, filter and save your favorites in the [interactive directory](https://abbosaliboev.github.io/free-ai-bible/catalog.html).', '']
    for category, (anchor, title) in sections.items():
        group = [r for r in reviewed if r['category'] == category and r['kind'] != 'paid']
        lines += [f'<a id="{anchor}"></a>', '', f'### {title}', '', '| Tool | What you can do | Free access |', '|---|---|---|']
        for r in group:
            summary, access = short.get(r['name'], (r['summary'], r['kind']))
            lines.append(f"| [**{r['name']}**]({r['url']}) | {summary} | {access} |")
        pending = [r for r in rows if r['category'] == category and r['verification'] != 'docs-reviewed']
        if pending:
            names = ' · '.join(f"[{r['name']}]({r['url']})" for r in pending)
            lines += ['', '<details>', '<summary>🔎 More tools to explore — current free access needs a fresh check</summary>', '', names, '', 'Check the current plan before signing up. [Help update an entry →](CONTRIBUTING.md)', '', '</details>']
        lines.append('')
    readme = (ROOT / 'README.md').read_text()
    start, rest = readme.split('<!-- CATALOG:START -->')
    _, end = rest.split('<!-- CATALOG:END -->')
    readme = start + '<!-- CATALOG:START -->\n' + '\n'.join(lines) + '\n<!-- CATALOG:END -->' + end
    out = io.StringIO(newline='')
    fields = list(rows[0])
    writer = csv.DictWriter(out, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    for r in rows:
        writer.writerow({**r, 'tags': ', '.join(r['tags'])})
    return {'README.md': readme, 'data/resources.csv': out.getvalue(), 'assets/catalog-data.js': 'window.AI_RESOURCES = ' + json.dumps(rows, ensure_ascii=False, indent=2) + ';\n'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    stale = []
    for path, content in render().items():
        target = ROOT / path
        if args.check:
            if not target.exists() or target.read_text() != content:
                stale.append(path)
        else:
            target.write_text(content)
    if stale:
        raise SystemExit('Regenerate catalog: python3 scripts/build-directory.py\n' + '\n'.join(stale))
    print('Catalog views are current.' if args.check else 'Generated README, CSV and browser data.')

if __name__ == '__main__':
    main()
