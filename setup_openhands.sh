#!/bin/bash
# Setup script untuk OpenHands SDK

echo "🚀 Menginstall OpenHands SDK..."

# Install dengan upgrade untuk kompatibilitas
pip install --upgrade openhands-sdk openhands-tools openhands-workspace

echo ""
echo "✅ Install selesai!"
echo ""
echo "📝 Untuk menjalankan:"
echo "   export OPENHANDS_CLOUD_API_KEY='sk-oh-your-key'"
echo "   python contoh_openhands_cloud.py"
echo ""
echo "📋 Cek versi:"
echo "   pip show openhands-sdk"
echo "   pip show openhands-workspace"
