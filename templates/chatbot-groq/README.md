# Streaming chatbot — Groq

A small CLI chatbot with streaming responses and conversation history.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
export GROQ_API_KEY=your_key_here
# Optional: choose another model available to your account
export GROQ_MODEL=openai/gpt-oss-20b
python app.py
```

Get a key at [Groq](https://console.groq.com). The default model is configurable because model availability changes. [Free limits](https://console.groq.com/docs/rate-limits) apply to both requests and tokens; this example is not a capacity guarantee. Prompts are sent to Groq. History grows during the session, so restart for a fresh context. Network/API errors currently stop the example.
