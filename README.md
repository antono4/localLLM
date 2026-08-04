# 🤖 AI Chat Assistant

Aplikasi chat AI dengan OpenAI API integration.

## 🚀 Cara Menjalankan

### 1. Install Dependencies

```bash
npm install
```

### 2. Jalankan Server

```bash
npm start
# atau
node server.js
```

### 3. Buka di Browser

Buka browser dan pergi ke:
```
http://localhost:3000
```

### 4. Masukkan API Key

1. Dapatkan API key dari [OpenAI Platform](https://platform.openai.com/api-keys)
2. Masukkan API key di kolom yang tersedia
3. Klik **Connect**
4. Mulai chat!

## 📁 Struktur File

```
localLLM/
├── index.html      # Frontend (HTML/CSS/JS)
├── server.js      # Backend server
├── package.json    # Dependencies
└── README.md      # Dokumentasi
```

## ⚙️ Requirements

- Node.js 14+
- OpenAI API Key

## 💡 Cara Kerja

1. Frontend (index.html) mengirim pesan ke backend
2. Backend (server.js) meneruskan ke OpenAI API
3. Response dari OpenAI dikirim kembali ke frontend
4. Chat displayed di browser

## 🔧 Troubleshooting

### "Server tidak berjalan"
Pastikan server sudah dijalankan:
```bash
node server.js
```

### "API Error"
- Cek API key valid
- Cek quota API cukup
- Cek koneksi internet

### CORS Error
Server sudah di-configure dengan CORS, jadi seharusnya tidak ada masalah.

## 📝 Catatan

- API key disimpan di localStorage browser (tidak dikirim ke server manapun selain OpenAI)
- Server hanya berfungsi sebagai proxy untuk menghindari CORS
- Semua request ke OpenAI dihandle oleh server

## 🌐 Demo Online

Jika tidak ingin install, coba versi online:
**https://antono4.github.io/localLLM/**

Tapi versi online tidak bisa connect ke API karena keterbatasan CORS.

## 📜 Lisensi

MIT License
