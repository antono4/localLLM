#!/usr/bin/env python3
"""
Diagnostic script untuk cek instalasi OpenHands
"""

import sys

def check_installation():
    print("=" * 60)
    print("🔍 OpenHands Installation Diagnostic")
    print("=" * 60)
    print()
    
    print(f"🐍 Python: {sys.version.split()[0]}")
    print()
    
    # Cek packages
    packages = {
        'openhands-sdk': None,
        'openhands-tools': None,
        'openhands-workspace': None,
    }
    
    import importlib.metadata
    for pkg in packages:
        try:
            ver = importlib.metadata.version(pkg)
            packages[pkg] = ver
            print(f"✅ {pkg}: {ver}")
        except importlib.metadata.PackageNotFoundError:
            print(f"❌ {pkg}: TIDAK TERINSTALL")
    
    print()
    print("=" * 60)
    print("🔧 Import Tests")
    print("=" * 60)
    print()
    
    # Test imports
    tests = [
        ('openhands.sdk', ['Agent', 'Conversation', 'LLM']),
        ('openhands.workspace', ['OpenHandsCloudWorkspace']),
        ('openhands.workspace.cloud', ['OpenHandsCloudWorkspace']),
    ]
    
    all_passed = True
    for module, classes in tests:
        print(f"📦 {module}:")
        try:
            mod = __import__(module, fromlist=classes)
            for cls in classes:
                if hasattr(mod, cls):
                    print(f"   ✅ {cls}")
                else:
                    available = [x for x in dir(mod) if not x.startswith('_')]
                    print(f"   ❌ {cls} (available: {available[:5]}...)")
                    all_passed = False
        except ImportError as e:
            print(f"   ❌ Import error: {e}")
            all_passed = False
        print()
    
    print("=" * 60)
    if all_passed:
        print("✅ Semua import BERHASIL!")
        print()
        print("📝 Untuk menjalankan:")
        print("   python contoh_openhands_cloud.py")
    else:
        print("❌ Ada masalah dengan instalasi")
        print()
        print("📌 SOLUSI:")
        print("=" * 60)
        print()
        print("1. Uninstall semua packages lama:")
        print("   pip uninstall openhands-sdk openhands-tools openhands-workspace -y")
        print()
        print("2. Clear pip cache:")
        print("   pip cache purge")
        print()
        print("3. Install ulang dengan pip:")
        print("   pip install openhands-sdk openhands-tools openhands-workspace")
        print()
        print("   ATAU dengan uv:")
        print("   pip install uv")
        print("   uv pip install openhands-sdk openhands-tools openhands-workspace")
        print()
        print("4. Cek Python version (rekomendasi: 3.10 - 3.12):")
        print("   python --version")
    
    print()
    print("=" * 60)

if __name__ == '__main__':
    check_installation()
