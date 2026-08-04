#!/bin/bash
# Setup script untuk OpenHands SDK
# Otomatis menggunakan uv jika tersedia

echo "============================================"
echo "🚀 OpenHands SDK Setup"
echo "============================================"
echo ""

# Fungsi untuk install packages
install_packages() {
    echo "📦 Menginstall packages..."
    echo ""
    
    # List packages
    PACKAGES="openhands-sdk openhands-tools openhands-workspace"
    
    if command -v uv &> /dev/null; then
        echo "✅ uv ditemukan! Menggunakan uv untuk install..."
        echo ""
        uv pip install $PACKAGES
    elif command -v conda &> /dev/null; then
        echo "✅ conda ditemukan! Menggunakan conda..."
        echo ""
        pip install $PACKAGES
    else
        echo "📝 Menggunakan pip untuk install..."
        echo ""
        pip install --upgrade $PACKAGES
    fi
    
    echo ""
    echo "============================================"
    echo "📋 Informasi Install"
    echo "============================================"
    pip show openhands-sdk 2>/dev/null | grep -E "^(Name|Version):"
    pip show openhands-workspace 2>/dev/null | grep -E "^(Name|Version):"
}

# Cek Python version
echo "🐍 Python version:"
python --version
echo ""

# Cek apakah packages sudah ada
if pip show openhands-sdk &> /dev/null; then
    echo "📌 openhands-sdk sudah terinstall:"
    pip show openhands-sdk | grep Version
    echo ""
    read -p "Upgrade? (y/n): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        install_packages
    fi
else
    echo "📦 openhands-sdk belum terinstall"
    install_packages
fi

echo ""
echo "============================================"
echo "✅ Setup selesai!"
echo "============================================"
echo ""
echo "📝 Untuk menjalankan:"
echo "   export OPENHANDS_CLOUD_API_KEY='sk-oh-your-key'"
echo "   python contoh_openhands_cloud.py"
echo ""
