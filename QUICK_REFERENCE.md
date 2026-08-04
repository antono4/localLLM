# 📋 Quick Reference - OpenHands SDK

## 🚀 Start Fast

```bash
# Pilihan 1: OpenHands Cloud (dengan cloud sandbox)
export OPENHANDS_CLOUD_API_KEY='sk-oh-your-cloud-key'
export LLM_API_KEY='sk-your-openai-anthropic-key'
python contoh_openhands_cloud.py

# Pilihan 2: Standalone SDK (tanpa cloud)
export OPENAI_API_KEY='sk-your-key-here'
python contoh_openhands.py
```

## 📁 File yang Dibuat

| File | Deskripsi |
|------|-----------|
| `OPENHANDS_LOKAL.md` | Panduan lengkap |
| `contoh_openhands.py` | Contoh dasar standalone |
| `contoh_docker_sandbox.py` | Contoh dengan Docker sandbox |
| `QUICK_REFERENCE.md` | Referensi cepat |

## 🔧 Command Penting

```bash
# Install SDK
pip install openhands-sdk openhands-tools

# Install dengan Docker support
pip install 'openhands-sdk[docker]'

# Upgrade
pip install --upgrade openhands-sdk
```

## 💡 Model yang Didukung

| Provider | Model | Contoh |
|----------|-------|--------|
| OpenAI | gpt-4o, gpt-4-turbo, gpt-3.5-turbo | `model='gpt-4o'` |
| Anthropic | claude-sonnet, claude-opus | `model='claude-sonnet-4-20250514'` |
| Google | gemini-2.0-flash, gemini-pro | `model='gemini-2.0-flash'` |
| Local (Ollama) | llama3, mistral, dll | `model='llama3', base_url='http://localhost:11434/v1'` |

## 🔐 Keamanan

```python
# Konfirmasi setiap aksi (recommended untuk production)
from openhands.sdk.security import ConfirmationLevel

agent = Agent(
    llm=llm,
    tools=[TerminalTool, FileEditorTool],
    confirmation_level=ConfirmationLevel.CONFIRM,
)
```

## 📊 Monitoring

```python
# Get metrics
metrics = conversation.get_metrics()
print(f"Total tokens: {metrics.total_tokens}")
print(f"Cost: ${metrics.total_cost}")

# Streaming response
for event in conversation.run(stream=True):
    print(event.content, end='', flush=True)
```

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| `No module named 'openhands'` | `pip install openhands-sdk openhands-tools` |
| `API key not found` | `export OPENAI_API_KEY='sk-...'` |
| Docker error | `sudo usermod -aG docker $USER` |

## 📚 Dokumentasi

- Website: https://docs.openhands.dev/
- SDK: https://docs.openhands.dev/sdk
- GitHub: https://github.com/OpenHands/software-agent-sdk
