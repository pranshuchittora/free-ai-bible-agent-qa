"""
Free RAG pipeline: Ollama (local LLM) + Chroma (local vector DB).
No API keys. Uses local models and an in-memory database in this configuration.

Prerequisites:
  - Ollama running: ollama serve
  - Model pulled: ollama pull qwen3:4b
  - Embedding model: ollama pull nomic-embed-text
  - pip install -r requirements.txt
"""

import uuid
import chromadb
from chromadb.utils.embedding_functions import OllamaEmbeddingFunction
from ollama import Client

OLLAMA_HOST = "http://localhost:11434"
MODEL = "qwen3:4b"
EMBED_MODEL = "nomic-embed-text"
COLLECTION_NAME = "my_docs"

ollama = Client(host=OLLAMA_HOST)
chroma = chromadb.Client()
embed_fn = OllamaEmbeddingFunction(url=OLLAMA_HOST, model_name=EMBED_MODEL)
collection = chroma.get_or_create_collection(COLLECTION_NAME, embedding_function=embed_fn)


def add_documents(docs: list[str], ids: list[str] | None = None) -> None:
    if ids is None:
        ids = [str(uuid.uuid4()) for _ in docs]
    collection.add(documents=docs, ids=ids)
    print(f"✅ Added {len(docs)} document(s) to the knowledge base.")


def query(question: str, n_results: int = 3) -> str:
    count = collection.count()
    if count == 0:
        return "I don't know. No documents have been added."
    results = collection.query(query_texts=[question], n_results=min(max(1, n_results), count))
    context = "\n\n".join(results["documents"][0])

    prompt = f"""Answer the question using only the context below.
If the answer isn't in the context, say "I don't know."

Context:
{context}

Question: {question}
Answer:"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


if __name__ == "__main__":
    # Example: load some documents
    sample_docs = [
        "Groq offers a model-specific free tier; check its official rate-limit documentation.",
        "Ollama lets you run LLMs locally with a single command: ollama run qwen3:4b.",
        "Chroma is an open-source vector database that runs entirely in-memory or on disk.",
        "The free AI Bible is a curated list of free AI tools and APIs for developers.",
    ]
    add_documents(sample_docs)

    print("\n🔍 RAG Pipeline Ready — ask anything about your documents.")
    print("   Type 'exit' to quit\n")

    while True:
        q = input("Question: ").strip()
        if q.lower() in ("exit", "quit"):
            break
        if not q:
            continue
        answer = query(q)
        print(f"\nAnswer: {answer}\n")
