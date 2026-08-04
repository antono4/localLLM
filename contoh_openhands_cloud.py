#!/usr/bin/env python3
"""
OpenHands Cloud Workspace - Contoh Lengkap
==========================================
Menggunakan OpenHands Cloud dengan SDK

API Key: sk-oh-... (OpenHands Cloud)
Environment: OPENHANDS_CLOUD_API_KEY
"""

import os
import sys

def main():
    # Ambil API key dari environment
    api_key = os.getenv('OPENHANDS_CLOUD_API_KEY') or os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ ERROR: OPENHANDS_CLOUD_API_KEY tidak ditemukan!")
        print("\n📌 Set dengan:")
        print("   export OPENHANDS_CLOUD_API_KEY='sk-oh-...'")
        print("\n   Atau gunakan:")
        print("   export OPENAI_API_KEY='sk-oh-...'")
        sys.exit(1)
    
    if not api_key.startswith('sk-oh-'):
        print("❌ ERROR: Butuh OpenHands Cloud API key (sk-oh-...)")
        print(f"   Key Anda: {api_key[:15]}...")
        print("   Buka https://app.all-hands.dev untuk mendapatkan API key")
        sys.exit(1)
    
    print("=" * 60)
    print("🚀 OPENHANDS CLOUD WORKSPACE")
    print("=" * 60)
    print(f"API Key: {api_key[:15]}...\n")
    
    # Suppress banner
    os.environ['OPENHANDS_SUPPRESS_BANNER'] = '1'
    
    # Import dengan fallback untuk kompatibilitas versi
    OpenHandsCloudWorkspace = None
    get_default_agent = None
    
    # Coba import dari openhands.workspace (standalone package)
    try:
        from openhands.workspace.cloud import OpenHandsCloudWorkspace
        print("✓ Using openhands.workspace package")
    except ImportError:
        # Fallback: coba dari openhands.sdk.workspace
        try:
            from openhands.sdk.workspace.cloud import OpenHandsCloudWorkspace
            print("✓ Using openhands.sdk.workspace (cloud submodule)")
        except ImportError:
            pass
    
    # Coba import get_default_agent
    try:
        from openhands.tools.preset.default import get_default_agent
    except ImportError:
        try:
            from openhands.sdk.agent import get_default_agent
        except ImportError:
            pass
    
    # Check imports
    if OpenHandsCloudWorkspace is None:
        print("❌ ERROR: Tidak bisa import OpenHandsCloudWorkspace")
        print("\n📌 Pastikan install dengan:")
        print("   pip install openhands-sdk openhands-tools openhands-workspace")
        print("\n📌 Atau upgrade semua packages:")
        print("   pip install --upgrade openhands-sdk openhands-tools openhands-workspace")
        sys.exit(1)
    
    if get_default_agent is None:
        print("⚠️  WARNING: Tidak bisa import get_default_agent")
        print("   Akan coba menggunakan Agent langsung...")
        from openhands.sdk import Agent, LLM
        get_default_agent = lambda llm, cli_mode: Agent(llm=llm)
    
    print("📦 Membuat Cloud Workspace...")
    
    try:
        # Connect ke OpenHands Cloud
        with OpenHandsCloudWorkspace(
            cloud_api_url="https://app.all-hands.dev",
            cloud_api_key=api_key,
        ) as workspace:
            
            print("✓ Cloud workspace berhasil dibuat!")
            print()
            
            # Test command execution
            result = workspace.execute_command("echo 'Hello from OpenHands Cloud!' && date")
            print(f"📨 Command output: {result.stdout.strip()}")
            
            # Dapatkan LLM dari cloud workspace (managed LLM)
            print("\n🔑 Menggunakan LLM dari OpenHands Cloud...")
            llm = workspace.get_llm()
            print(f"   LLM: {llm.model}")
            
            # Dapatkan agent dengan LLM dari cloud
            agent = get_default_agent(llm=llm, cli_mode=True)
            
            # Buat conversation
            conversation = Conversation(
                agent=agent,
                workspace=workspace
            )
            
            # Kirim tugas
            task = """Buat file 'test_cloud.txt' yang berisi:
1. "OpenHands Cloud Workspace BERHASIL!"
2. Tanggal dan waktu saat ini
3. "Test dari Python SDK"
"""
            
            print("\n📝 Mengirim tugas ke OpenHands Cloud...")
            print("-" * 50)
            
            conversation.send_message(task)
            conversation.run()
            
            print("-" * 50)
            print("\n✅ Selesai!")
            print("\n📄 File telah dibuat di cloud workspace")
            
    except KeyboardInterrupt:
        print("\n\n⚠️ Dihentikan oleh user")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("\n📌 Kemungkinan penyebab:")
        print("   - API key invalid atau expired")
        print("   - Quota habis")
        print("   - Koneksi internet bermasalah")
        print("\n📚 Buka https://app.all-hands.dev untuk cek status akun")

if __name__ == '__main__':
    main()
