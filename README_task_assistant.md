# 🤖 AI Task Assistant - Local LLM Edition

Aplikasi automasi tugas berbasis AI menggunakan **OpenHands Cloud** untuk membantu developer mengotomatisasi berbagai tugas pemrograman.

## ✨ Fitur

- **Preset Tasks**: Tugas-tugas umum yang siap dijalankan
- **Custom Tasks**: Jalankan tugas kustom sesuai kebutuhan
- **Interactive Mode**: Mode interaktif untuk berbagai tugas
- **Cloud Powered**: Menggunakan OpenHands Cloud dengan LLM yang dikelola

## 🚀 Instalasi

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Atau install manual:

```bash
pip install openhands-sdk openhands-tools openhands-workspace
```

### 2. Set API Key

Dapatkan API key dari [OpenHands Cloud](https://app.all-hands.dev):

```bash
export OPENHANDS_CLOUD_API_KEY='sk-oh-your-key-here'
```

## 📖 Penggunaan

### Preset Tasks

```bash
# Buat file hello
python task_assistant.py --task hello

# Buat README untuk project
python task_assistant.py --task readme

# Backup semua file Python
python task_assistant.py --task backup

# Analisis struktur code
python task_assistant.py --task analyze

# Clean temporary files
python task_assistant.py --task clean

# Generate unit tests
python task_assistant.py --task test

# Generate documentation
python task_assistant.py --task docs

# Security scan
python task_assistant.py --task security
```

### Custom Task

```bash
# Jalankan tugas kustom
python task_assistant.py --custom "Buat Flask app dengan endpoint /api/users"

# Contoh lainnya
python task_assistant.py --custom "Buat CLI tool untuk manage database migrations"
python task_assistant.py --custom "Buat script untuk auto-deploy ke server"
```

### Interactive Mode

```bash
# Mode interaktif
python task_assistant.py --interactive

# Di dalam interactive mode:
# - Ketik tugas yang ingin dijalankan
# - Ketik 'help' untuk bantuan
# - Ketik 'exit' untuk keluar
```

### Lewat Python Code

```python
from task_assistant import TaskAssistant

# Initialize dengan API key
assistant = TaskAssistant(api_key='sk-oh-your-key')

# Connect
assistant.connect()

# Jalankan preset task
assistant.run_preset_task('hello')

# Atau custom task
assistant.execute_task("Buat program CLI untuk todo list")

# Cleanup
assistant.disconnect()
```

## 📝 Preset Tasks

| Task | Deskripsi |
|------|-----------|
| `hello` | Buat file hello.txt dengan sapaan |
| `readme` | Generate README.md untuk project |
| `backup` | Backup semua file .py ke folder backup/ |
| `analyze` | Analisis struktur code dan generate laporan |
| `clean` | Hapus file temporary dan buat .gitignore |
| `test` | Generate unit tests untuk main.py |
| `docs` | Tambahkan docstring dan comments |
| `security` | Security scan dan generate laporan |

## 🔐 Keamanan

- API key disimpan di environment variable, tidak di-hardcode
- Semua aksi dijalankan di sandbox cloud
- Support confirmation mode untuk approve setiap aksi

## 🐛 Troubleshooting

### Error: "Package not found"

```bash
pip install --upgrade openhands-sdk openhands-tools openhands-workspace
```

### Error: "API key not found"

```bash
export OPENHANDS_CLOUD_API_KEY='sk-oh-your-key'
```

### Error: Connection failed

- Cek koneksi internet
- Pastikan API key valid
- Buka https://app.all-hands.dev untuk cek status

## 📚 Referensi

- [OpenHands Documentation](https://docs.openhands.dev/)
- [OpenHands SDK](https://docs.openhands.dev/sdk)
- [OpenHands Cloud](https://app.all-hands.dev)

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan buat pull request atau issue.

## 📄 Lisensi

MIT License

---

*Made with ❤️ using OpenHands Cloud*
