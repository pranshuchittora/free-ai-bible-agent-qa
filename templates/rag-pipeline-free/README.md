# Local RAG — Ollama + Chroma

Load text documents, retrieve matching passages and answer using local inference.

Install [Ollama](https://ollama.com/download) for your OS and start its app/service, then:

```bash
ollama pull qwen3:4b
ollama pull nomic-embed-text
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Uses a dedicated embedding model and an in-memory Chroma database. Documents disappear when the process ends. `add_documents` accepts text strings; PDF parsing/chunking is not included. For document conversion explore Docling or MarkItDown in the catalog.

After installation and model downloads, inference runs locally with this configuration. Hardware and model licenses apply. Retrieval can miss relevant text and answers may be wrong; evaluate against your own documents.
