#!/usr/bin/env python3
"""
OpenHands Cloud Workspace - Versi Simple
=======================================
Tanpa import OpenHandsCloudWorkspace
Hanya gunakan command execution untuk testing
"""

import os
import sys

def main():
    # Cek API key
    api_key = os.getenv('OPENHANDS_CLOUD_API_KEY') or os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ ERROR: OPENHANDS_CLOUD_API_KEY tidak ditemukan!")
        print("\n📌 Set dengan:")
        print("   export OPENHANDS_CLOUD_API_KEY='sk-oh-...'")
        sys.exit(1)
    
    if not api_key.startswith('sk-oh-'):
        print("❌ ERROR: Butuh OpenHands Cloud API key (sk-oh-...)")
        sys.exit(1)
    
    print("=" * 60)
    print("🚀 OPENHANDS CLOUD WORKSPACE")
    print("=" * 60)
    print(f"API Key: {api_key[:15]}...\n")
    
    os.environ['OPENHANDS_SUPPRESS_BANNER'] = '1'
    
    # Import SDK
    try:
        from openhands.sdk.workspace.cloud import OpenHandsCloudWorkspace
        print("✓ Found OpenHandsCloudWorkspace in openhands.sdk.workspace.cloud")
    except ImportError:
        try:
            from openhands.workspace.cloud import OpenHandsCloudWorkspace
            print("✓ Found OpenHandsCloudWorkspace in openhands.workspace.cloud")
        except ImportError as e:
            print(f"❌ ERROR: {e}")
            print("\n" + "=" * 60)
            print("📌 INSTALASI:")
            print("=" * 60)
            print("pip install --upgrade openhands-sdk openhands-tools openhands-workspace")
            print("\n📌 Atau cek versi:")
            print("pip show openhands-sdk")
            print("pip show openhands-workspace")
            sys.exit(1)
    
    print("\n📦 Membuat Cloud Workspace...")
    
    try:
        with OpenHandsCloudWorkspace(
            cloud_api_url="https://app.all-hands.dev",
            cloud_api_key=api_key,
        ) as workspace:
            
            print("✓ Cloud workspace berhasil dibuat!")
            print()
            
            # Test command
            result = workspace.execute_command("echo 'Hello!' && date && whoami")
            print(f"📨 Output:\n{result.stdout}")
            
            # Dapatkan LLM dari cloud
            print("\n🔑 Mengambil LLM dari cloud...")
            llm = workspace.get_llm()
            print(f"   Model: {llm.model}")
            
            # Buat agent
            print("\n🤖 Membuat agent...")
            from openhands.tools.preset.default import get_default_agent
            agent = get_default_agent(llm=llm, cli_mode=True)
            
            # Conversation
            from openhands.sdk import Conversation
            conversation = Conversation(agent=agent, workspace=workspace)
            
            # Kirim tugas
            print("\n📝 Mengirim tugas...")
            conversation.send_message("Buat file 'hasil.txt' yang berisi 'Berhasil!' dan tanggal saat ini")
            conversation.run()
            
            print("\n✅ Selesai!")
            
    except KeyboardInterrupt:
        print("\n\n⚠️ Dihentikan")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
