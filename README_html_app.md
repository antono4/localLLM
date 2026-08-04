# 🤖 AI Task Assistant - Web Version

Aplikasi **AI Task Assistant** versi web berbasis HTML/CSS/JavaScript yang menggunakan **OpenHands Cloud API** untuk mengotomatisasi berbagai tugas pemrograman.

## ✨ Fitur

- **Web-based Interface**: Antarmuka modern dan responsif
- **Preset Tasks**: 8 tugas umum siap dijalankan
- **Custom Tasks**: Jalankan tugas kustom sesuai kebutuhan
- **Real-time Output**: Output langsung di browser
- **Dark Theme**: Desain modern dengan dark mode
- **Responsive**: Tampil bagus di desktop dan mobile

## 🚀 Cara Menjalankan

### Opsi 1: Langsung di Browser
Buka file `index.html` langsung di browser Anda:
```bash
# macOS
open index.html

# Linux
xdg-open index.html

# Windows
start index.html
```

### Opsi 2: Local Server (Recommended)
```bash
# Python 3
python -m http.server 8000

# Node.js
npx serve .

# PHP
php -S localhost:8000
```

Luego abra en su navegador: `http://localhost:8000`

## 🔑 Konfigurasi API Key

1. Obtenga su API key de [OpenHands Cloud](https://app.all-hands.dev)
2. Ingrese el API key en el campo de configuración
3. Haga clic en "Simpan" para guardar
4. Haga clic en "Test Koneksi" para verificar

## 📝 Preset Tasks

| Task | Deskripsi |
|------|-----------|
| 👋 Hello | Buat file sapaan sederhana |
| 📄 README | Generate README.md untuk project |
| 💾 Backup | Backup semua file Python |
| 🔍 Analyze | Analisis struktur code |
| 🧹 Clean | Hapus file temporary |
| 🧪 Test | Generate unit tests |
| 📚 Docs | Generate dokumentasi |
| 🔒 Security | Security scan |

## 🎨 Custom Task

Gunakan textarea untuk menulis tugas kustom:
```javascript
// Contoh
"Buat program CLI untuk manage todo list"
"Buat Flask app dengan endpoint /api/users"
"Generate unit test untuk semua function"
```

## 📁 Struktur File

```
localLLM/
├── index.html              # Aplikasi utama
├── README_html_app.md      # Dokumentasi
├── task_assistant.py       # Versi Python CLI
├── requirements.txt        # Dependencies Python
└── *.py                    # Contoh-contoh lain
```

## 🔧 API Integration

Aplikasi menggunakan OpenHands Cloud API:
- **API URL**: `https://app.all-hands.dev/api`
- **Auth**: Bearer Token (API Key)
- **Method**: REST API

```javascript
// Contoh request
fetch(`${API_URL}/conversations`, {
    method: 'POST',
    headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ model: 'claude-sonnet-4-20250514' })
});
```

## 🎯 Usage Examples

### 1. Generate Hello File
1. Masukkan API Key
2. Klik tombol "Hello"
3. Lihat output di panel kanan

### 2. Analyze Project
1. Pilih preset task "Analyze"
2. Tunggu proses selesai
3. Lihat laporan struktur code

### 3. Custom Task
1. Ketik tugas di textarea
2. Klik "Jalankan Tugas Kustom"
3. Lihat hasil real-time

## 🛡️ Keamanan

- API key disimpan di localStorage browser
- Tidak ada data yang dikirim ke server lain
- Semua request langsung ke OpenHands Cloud
- Support untuk HTTPS only

## 📱 Responsive Design

| Breakpoint | Layout |
|------------|--------|
| Desktop (>768px) | 2 columns side-by-side |
| Mobile (<768px) | Stacked vertically |

## 🎨 Color Palette

```css
--primary: #6366f1        /* Indigo */
--secondary: #10b981      /* Emerald */
--bg-dark: #0f172a       /* Slate 900 */
--bg-card: #1e293b       /* Slate 800 */
--text-primary: #f1f5f9   /* Slate 100 */
--text-secondary: #94a3b8 /* Slate 400 */
```

## 🐛 Troubleshooting

### "API Key not found"
- Pastikan API key sudah diinput
- Klik "Simpan" setelah input

### "Connection failed"
- Cek koneksi internet
- Pastikan API key valid
- Buka https://app.all-hands.dev untuk verifikasi

### Output tidak muncul
- Cek console browser (F12)
- Refresh halaman
- Pastikan JavaScript enabled

## 📚 Referensi

- [OpenHands Documentation](https://docs.openhands.dev/)
- [OpenHands Cloud](https://app.all-hands.dev)
- [Repository](https://github.com/antono4/localLLM)

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan buat issue atau pull request.

## 📄 Lisensi

MIT License

---

*Made with ❤️ using OpenHands Cloud API*
