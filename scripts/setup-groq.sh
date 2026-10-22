#!/bin/bash
# One-click Groq setup: installs SDK and runs a test query

set -e

echo "🚀 Setting up Groq (Free LLM API — model-specific limits)..."
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Install it from https://python.org"
    exit 1
fi

# Install SDK
python3 -m pip install groq --quiet
echo "✅ Groq SDK installed"

# Prompt for key
echo ""
echo "👉 Get your free API key at: https://console.groq.com"
echo ""
read -r -s -p "Paste your Groq API key here (hidden): " GROQ_KEY
echo ""

if [ -z "$GROQ_KEY" ]; then
    echo "❌ No key provided. Exiting."
    exit 1
fi

# Export for this session
export GROQ_API_KEY="$GROQ_KEY"

# Do not persist secrets or modify the user's shell configuration.
echo "✅ Key set for this setup process only."
echo "   For other terminals, set GROQ_API_KEY with your preferred secret manager."

# Test it
echo ""
echo "🧪 Running test query..."
python3 - <<'EOF'
import os
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])
response = client.chat.completions.create(
    model=os.environ.get("GROQ_MODEL", "openai/gpt-oss-20b"),
    messages=[{"role": "user", "content": "Say 'Groq setup successful!' and nothing else."}]
)
print("")
print("🎉", response.choices[0].message.content)
print("")
print("Your API connection works. Check the current model limits before building.")
EOF
