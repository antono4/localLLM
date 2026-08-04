#!/usr/bin/env python3
"""
Auto-fix script untuk OpenHands SDK
===================================
Uninstall versi lama dan install versi baru
"""

import subprocess
import sys

def run(cmd, desc=""):
    print(f"📦 {desc}...")
    print(f"   $ {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout[:500])
    if result.returncode != 0:
        print(f"❌ ERROR: {result.stderr[:300]}")
        return False
    return True

def check_versions():
    print("=" * 60)
    print("🔍 Cek Versi Sekarang")
    print("=" * 60)
    run("pip show openhands-sdk", "openhands-sdk version")
    run("pip show openhands-workspace", "openhands-workspace version")
    print()

def main():
    print("=" * 60)
    print("🔧 OpenHands SDK Auto-Fix")
    print("=" * 60)
    print()
    
    # Step 1: Check current versions
    check_versions()
    
    # Step 2: Uninstall old packages
    print("=" * 60)
    print("🗑️ Uninstall versi lama")
    print("=" * 60)
    run("pip uninstall openhands-sdk openhands-tools openhands-workspace -y", "Uninstall packages")
    print()
    
    # Step 3: Clear cache
    print("=" * 60)
    print("🧹 Clear pip cache")
    print("=" * 60)
    run("pip cache purge", "Clear cache")
    print()
    
    # Step 4: Install fresh
    print("=" * 60)
    print("📦 Install versi terbaru")
    print("=" * 60)
    print()
    print("   pip install openhands-sdk openhands-tools openhands-workspace")
    print()
    
    result = subprocess.run(
        "pip install openhands-sdk openhands-tools openhands-workspace",
        shell=True, capture_output=True, text=True
    )
    
    if result.returncode != 0:
        print(f"❌ Install GAGAL: {result.stderr[:500]}")
        print()
        print("=" * 60)
        print("📌 Alternatif: Pakai uv")
        print("=" * 60)
        print("""
# Install uv dulu
pip install uv

# Atau download dari: https://github.com/astral-sh/uv/releases

# Lalu install dengan uv
uv pip install openhands-sdk openhands-tools openhands-workspace
""")
        return
    
    print("✅ Install BERHASIL!")
    print()
    
    # Step 5: Verify
    print("=" * 60)
    print("✅ Verifikasi")
    print("=" * 60)
    run("pip show openhands-sdk | findstr Version", "Cek versi SDK")
    print()
    
    # Test import
    print("🧪 Test import...")
    result = subprocess.run(
        "python -c \"from openhands.sdk.workspace import PlatformType; print('OK')\"",
        shell=True, capture_output=True, text=True
    )
    
    if result.returncode == 0:
        print("✅ Import BERHASIL!")
    else:
        print("❌ Import GAGAL")
        print("   Cek apakah masih ada cache lama:")
        print("   pip cache purge")
        print("   python -m pip cache purge")
    
    print()
    print("=" * 60)
    print("📝 Langkah selanjutnya:")
    print("=" * 60)
    print("""
$env:OPENHANDS_CLOUD_API_KEY = "sk-oh-BHQj5RRY9flnWdaVIkFSUwRCg8YAtGzQ"
python contoh_openhands_cloud.py
""")

if __name__ == '__main__':
    main()
