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
    
    try:
        from openhands.workspace.cloud import OpenHandsCloudWorkspace
        from openhands.sdk import LLM, Conversation
        from openhands.tools.preset.default import get_default_agent
    except ImportError as e:
        print(f"❌ ERROR importing: {e}")
        print("\n📌 Pastikan install dengan:")
        print("   pip install openhands-workspace")
        sys.exit(1)
    
    # LLM API Key - HARUS dari OpenAI atau Anthropic
    # BUKAN OpenHands Cloud key (sk-oh-...)
    llm_api_key = os.getenv('LLM_API_KEY') or os.getenv('OPENAI_API_KEY')
    
    if not llm_api_key:
        print("❌ ERROR: LLM_API_KEY tidak ditemukan!")
        print("\n📌 UNTUK MENJALANKAN AGENT, ANDA MEMBUTUHKAN:")
        print("   - LLM_API_KEY: OpenAI atau Anthropic API key")
        print("   - BUKAN OpenHands Cloud API key!")
        print("\n📝 Contoh:")
        print("   export LLM_API_KEY='sk-ant-...'  # Anthropic")
        print("   export LLM_API_KEY='sk-...'       # OpenAI")
        print()
        print("💡 Anda bisa mendapatkan API key di:")
        print("   - OpenAI: platform.openai.com")
        print("   - Anthropic: console.anthropic.com")
        sys.exit(1)
    
    if llm_api_key.startswith('sk-oh-'):
        print("❌ ERROR: Anda menggunakan OpenHands Cloud key sebagai LLM key!")
        print("   LLM_API_KEY harus dari OpenAI atau Anthropic")
        print("   BUKAN sk-oh-...")
        sys.exit(1)
    
    print(f"🔑 LLM API Key: {llm_api_key[:15]}...")
    llm = LLM(
        model=os.getenv('LLM_MODEL', 'claude-sonnet-4-20250514'),
        api_key=llm_api_key,
    )
    
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
            
            # Dapatkan agent
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
