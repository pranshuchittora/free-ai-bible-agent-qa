#!/bin/bash
# One-click Ollama setup: installs Ollama and pulls a configurable local model

set -e

echo "🦙 Setting up Ollama (Local LLM — offline inference after model download)..."
echo ""

OLLAMA_SETUP_OS="$(uname -s)"
OLLAMA_SETUP_MODEL="${OLLAMA_MODEL:-qwen3:4b}"

if [ "$OLLAMA_SETUP_OS" = "Darwin" ]; then
    if command -v brew &> /dev/null; then
        brew install ollama --quiet
    else
        echo "Install the macOS app from https://ollama.com/download, then rerun this script."
        exit 1
    fi
elif [ "$OLLAMA_SETUP_OS" = "Linux" ]; then
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "❌ Windows detected. Download Ollama from: https://ollama.com/download"
    exit 1
fi

echo "✅ Ollama installed"
echo ""

# Start Ollama service in background
ollama serve &>/dev/null &
sleep 2

# Pull model
echo "📦 Downloading $OLLAMA_SETUP_MODEL (size and RAM depend on model)..."
ollama pull "$OLLAMA_SETUP_MODEL"

echo ""
echo "✅ All done! Starting interactive chat..."
echo "   Type /bye to exit"
echo ""
ollama run "$OLLAMA_SETUP_MODEL"
