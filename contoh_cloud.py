#!/usr/bin/env python3
"""
OpenHands Cloud - Contoh Penggunaan
====================================
Script ini menghubungkan ke OpenHands Cloud menggunakan API key.

API Key Format: sk-oh-XXXXX (OpenHands Cloud)
"""

import os
import sys

def main():
    # Ambil API key
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY tidak ditemukan!")
        print("   Set dengan: export OPENAI_API_KEY='sk-oh-...'")
        sys.exit(1)
    
    print(f"🔑 API Key: {api_key[:10]}...")
    
    # Check if OpenHands Cloud key
    if api_key.startswith('sk-oh-'):
        print("✓ OpenHands Cloud API key detected\n")
        
        try:
            # Import OpenHands SDK
            from openhands.sdk import Agent, Conversation
            from openhands.sdk.llm import LLM
        except ImportError as e:
            print(f"❌ ERROR: {e}")
            print("   Install: pip install openhands-sdk")
            sys.exit(1)
        
        # Untuk OpenHands Cloud, Anda perlu endpoint server
        # Dalam kasus ini, kita bisa menggunakan OpenHands Cloud REST API
        
        print("""
📌 PILIHAN PENGGUNAAN OPENHANDS CLOUD:

Option 1: CLI Mode
-----------------
Gunakan OpenHands CLI untuk connect ke cloud:
   openhands --api-key $OPENAI_API_KEY

Option 2: Agent Server
---------------------
Jalankan agent server lokal yang terhubung ke cloud:
   openhands-server --api-key $OPENAI_API_KEY

Option 3: Langsung SDK (Butuh Konfigurasi Tambahan)
--------------------------------------------------
Jika Anda punya endpoint OpenHands Cloud yang spesifik:
   - Buka https://app.all-hands.dev
   - Dapatkan workspace endpoint
   - Konfigurasi SDK untuk connect ke sana

Option 4: Standalone dengan LLM langsung
--------------------------------------
Jika Anda ingin pakai SDK langsung tanpa cloud:
   - Butuh OpenAI/Anthropic API key
   - Edit script ini untuk pakai model LLM langsung
""")
        
        # Coba cek apakah ada config untuk cloud workspace
        print("\n🔍 Mencoba koneksi ke OpenHands Cloud...")
        
        # Metode 1: Via REST API
        import requests
        
        try:
            # OpenHands Cloud API endpoint
            response = requests.get(
                'https://app.all-hands.dev/api/status',
                headers={'Authorization': f'Bearer {api_key}'},
                timeout=5
            )
            
            if response.status_code == 200:
                print("✓ Koneksi ke OpenHands Cloud BERHASIL!")
                data = response.json()
                print(f"   Status: {data}")
            elif response.status_code == 401:
                print("⚠️ API key tidak valid atau expired")
            else:
                print(f"⚠️ Response: {response.status_code}")
                
        except Exception as e:
            print(f"⚠️ Tidak bisa connect langsung: {e}")
            print("\n📌 Gunakan CLI untuk akses OpenHands Cloud:")
            print("   $ openhands --help")
    
    else:
        # OpenAI/Anthropic key
        print("✓ Standard API key (OpenAI/Anthropic)")
        print("\nMenjalankan dengan LLM langsung...\n")
        
        # Lanjutkan dengan contoh standar
        from openhands.sdk import LLM, Agent, Conversation
        from openhands.tools.terminal import TerminalTool
        from openhands.tools.file_editor import FileEditorTool
        
        llm = LLM(
            model='gpt-4o',
            api_key=api_key,
        )
        
        agent = Agent(
            llm=llm,
            tools=[TerminalTool, FileEditorTool],
        )
        
        conversation = Conversation(
            agent=agent,
            workspace=os.getcwd()
        )
        
        conversation.send_message("Buat file test_openai.txt yang berisi 'OpenHands + OpenAI working!'")
        conversation.run()
        print("\n✅ Selesai!")

if __name__ == '__main__':
    main()
