# 🚀 Panduan Menjalankan OpenHands di Komputer Lokal

OpenHands adalah AI Agent yang dapat membantu Anda mengotomatisasi berbagai tugas pemrograman. Berikut adalah panduan lengkap untuk menjalankannya di komputer lokal Anda.

## 📋 Prasyarat

- **Python 3.10+** (Anda memiliki Python 3.13.14 ✓)
- **Docker** (Anda memiliki Docker 29.6.2 ✓) - Opsional, untuk sandboxing
- **API Keys**:

### Untuk OpenHands Cloud (Recommended)
- **OPENHANDS_CLOUD_API_KEY**: Dari https://app.all-hands.dev
- **LLM_API_KEY**: OpenAI atau Anthropic API key

### Untuk Standalone SDK
- **OPENAI_API_KEY** atau **ANTHROPIC_API_KEY**: Langsung ke provider LLM

## 🔧 Instalasi

### 1. Instal OpenHands SDK

```bash
pip install openhands-sdk openhands-tools
```

### 2. (Opsional) Instal Tools Tambahan

```bash
# Untuk browser automation
pip install openhands-tools[browser]

# Untuk semua fitur
pip install openhands-tools[all]
```

## 📝 Contoh Kode Sederhana

### Contoh 1: Hello World

```python
import os
from openhands.sdk import LLM, Agent, Conversation
from openhands.tools.terminal import TerminalTool
from openhands.tools.file_editor import FileEditorTool

# Konfigurasi LLM (Ganti dengan API key Anda)
llm = LLM(
    model='gpt-4o',
    api_key=os.getenv('OPENAI_API_KEY'),  # Atau set langsung: api_key='sk-...'
)

# Buat Agent dengan tools yang diperlukan
agent = Agent(
    llm=llm,
    tools=[
        TerminalTool,  # Untuk menjalankan perintah terminal
        FileEditorTool,  # Untuk membaca/menulis file
    ],
)

# Buat conversation dengan folder kerja saat ini
cwd = os.getcwd()
conversation = Conversation(agent=agent, workspace=cwd)

# Kirim tugas ke agent
conversation.send_message("Buatkan file HELLO.md yang berisi sapaan sederhana dan tanggal hari ini.")
conversation.run()

print("✅ Selesai! Lihat file HELLO.md")
```

### Contoh 2: Dengan Task Tracker

```python
import os
from openhands.sdk import LLM, Agent, Conversation
from openhands.tools.terminal import TerminalTool
from openhands.tools.file_editor import FileEditorTool
from openhands.tools.task_tracker import TaskTrackerTool

llm = LLM(
    model='gpt-4o',
    api_key=os.getenv('OPENAI_API_KEY'),
)

agent = Agent(
    llm=llm,
    tools=[TerminalTool, FileEditorTool, TaskTrackerTool],
)

conversation = Conversation(
    agent=agent, 
    workspace=os.getcwd()
)

conversation.send_message("""
Tugas:
1. Buat folder 'src' 
2. Di dalamnya buat file 'app.py' dengan fungsi hello()
3. Update task tracker dengan progres
""")
conversation.run()
```

### Contoh 3: Dengan Browser Automation

```python
import os
from openhands.sdk import LLM, Agent, Conversation
from openhands.tools.browser import BrowserTool

llm = LLM(
    model='gpt-4o',
    api_key=os.getenv('OPENAI_API_KEY'),
)

agent = Agent(
    llm=llm,
    tools=[BrowserTool],  # Memungkinkan agent browsing web
)

conversation = Conversation(agent=agent, workspace=os.getcwd())

conversation.send_message(
    "Buka Google dan cari berita terbaru tentang AI. "
    "Simpan 3 headline ke file 'berita.txt'"
)
conversation.run()
```

## 🐳 Menjalankan dengan Docker Sandbox (Recommended)

Untuk isolasi dan keamanan, Anda bisa menjalankan agent di dalam container Docker:

```python
import os
from openhands.sdk import LLM, Agent, Conversation
from openhands.sdk.sandbox.docker_sandbox import DockerSandbox

# Konfigurasi LLM
llm = LLM(
    model='gpt-4o',
    api_key=os.getenv('OPENAI_API_KEY'),
)

# Sandbox Docker
sandbox = DockerSandbox()

agent = Agent(
    llm=llm,
    tools=sandbox.get_tools(),  # Tools yang berjalan di dalam Docker
)

conversation = Conversation(agent=agent, workspace=sandbox.workspace)

conversation.send_message("Buatkan program Python sederhana untuk menghitung factorial")
conversation.run()

sandbox.close()  # Bersihkan resources
```

## ☁️ Menjalankan dengan OpenHands Cloud (Paling Mudah!)

**HANYA butuh OpenHands Cloud API key** - LLM sudah included!

```python
import os
from openhands.workspace.cloud import OpenHandsCloudWorkspace
from openhands.sdk import Conversation
from openhands.tools.preset.default import get_default_agent

# Set API key
api_key = os.getenv('OPENHANDS_CLOUD_API_KEY')

# Connect ke OpenHands Cloud
with OpenHandsCloudWorkspace(
    cloud_api_url="https://app.all-hands.dev",
    cloud_api_key=api_key,
) as workspace:
    
    # Dapatkan LLM dari cloud (managed, tanpa setup tambahan!)
    llm = workspace.get_llm()
    
    # Buat agent
    agent = get_default_agent(llm=llm, cli_mode=True)
    
    # Kirim tugas
    conversation = Conversation(agent=agent, workspace=workspace)
    conversation.send_message("Buat file hello.txt dengan sapaan")
    conversation.run()
```

Jalankan dengan:
```bash
export OPENHANDS_CLOUD_API_KEY='sk-oh-your-key'
python contoh_openhands_cloud.py
```

## 🔐 Konfigurasi Keamanan

### Menggunakan Confirmation Mode

Untuk approving setiap aksi sebelum dijalankan:

```python
from openhands.sdk.security import ConfirmationLevel

agent = Agent(
    llm=llm,
    tools=[TerminalTool, FileEditorTool],
    confirmation_level=ConfirmationLevel.CONFIRM,  # Konfirmasi setiap aksi
)
```

### Custom Security Policy

```python
from openhands.sdk.security import SecurityAnalyzer, Action

class MySecurityPolicy:
    def should_block(self, action: Action) -> bool:
        # Block perintah berbahaya
        dangerous = ['rm -rf /', 'format c:', 'del /f /s /q']
        return any(cmd in str(action) for cmd in dangerous)

agent = Agent(
    llm=llm,
    tools=[TerminalTool, FileEditorTool],
    security_analyzer=SecurityAnalyzer(custom_policy=MySecurityPolicy()),
)
```

## 📊 Monitoring & Debugging

### Enable Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)

conversation = Conversation(agent=agent, workspace=cwd)
```

### Streaming Response

```python
conversation = Conversation(agent=agent, workspace=cwd)

# Kirim pesan
conversation.send_message("Analisis file README.md")

# Streaming response
for event in conversation.run(stream=True):
    if hasattr(event, 'content'):
        print(event.content, end='', flush=True)
```

## 🔄 Opsi LLM Provider

### OpenAI
```python
llm = LLM(model='gpt-4o', api_key='sk-...')
```

### Anthropic (Claude)
```python
llm = LLM(
    model='claude-sonnet-4-20250514',
    api_key='sk-ant-...',
    base_url='https://api.anthropic.com'
)
```

### Local/Ollama
```python
llm = LLM(
    model='llama3',
    api_key='ollama',  # Dummy key untuk lokal
    base_url='http://localhost:11434/v1'
)
```

### Google Gemini
```python
llm = LLM(
    model='gemini-2.0-flash',
    api_key='AIza...',
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)
```

## 🎯 Tips & Best Practices

1. **Gunakan environment variable** untuk API keys:
   ```bash
   export OPENAI_API_KEY='sk-...'
   export ANTHROPIC_API_KEY='sk-ant-...'
   ```

2. **Mulai dengan task sederhana** untuk menguji setup

3. **Gunakan Docker sandbox** untuk keamanan saat menjalankan kode

4. **Monitor token usage** untuk mengontrol biaya:
   ```python
   metrics = conversation.get_metrics()
   print(f"Total tokens: {metrics.total_tokens}")
   ```

5. **Simpan conversation state** untuk resume nanti:
   ```python
   state = conversation.get_state()
   # Simpan ke file
   conversation2 = Conversation.from_state(state, agent=agent)
   ```

## 🚨 Troubleshooting

### Error: "No module named 'openhands'"
```bash
pip install --upgrade openhands-sdk openhands-tools
```

### Error: "API key not found"
```bash
export OPENAI_API_KEY='your-key-here'
python your_script.py
```

### Error: Docker permission denied
```bash
sudo usermod -aG docker $USER
# Logout dan login kembali
```

## 📚 Referensi Lanjutan

- [Dokumentasi Resmi](https://docs.openhands.dev/)
- [SDK Reference](https://docs.openhands.dev/sdk)
- [Examples](https://github.com/OpenHands/software-agent-sdk/tree/main/examples)

---

*Panduan ini dibuat untuk membantu Anda memulai dengan OpenHands. Untuk informasi lebih lanjut, kunjungi [docs.openhands.dev](https://docs.openhands.dev/)*
