#!/usr/bin/env python3
"""
Contoh OpenHands SDK - Docker Sandbox
======================================
Script ini mendemonstrasikan cara menjalankan OpenHands 
di dalam Docker container untuk isolasi dan keamanan.

KEUNGGULAN DOCKER SANDBOX:
- Kode agent dijalankan di environment terisolasi
- Tidak mempengaruhi sistem host secara langsung
- Lebih aman untuk testing kode dari internet

SEBELUM MENJALANKAN:
1. Pastikan Docker terinstall dan running
2. Set API key: export OPENAI_API_KEY='sk-...'
"""

import os
import sys

def main():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY tidak ditemukan!")
        print("\n📌 Set API key terlebih dahulu:")
        print("   $ export OPENAI_API_KEY='sk-your-key-here'")
        sys.exit(1)
    
    try:
        from openhands.sdk import LLM, Agent, Conversation
        from openhands.sdk.sandbox import DockerSandbox
    except ImportErrorError as e:
        print(f"❌ ERROR: {e}")
        print("   $ pip install openhands-sdk[docker]")
        sys.exit(1)
    except Exception as e:
        print(f"❌ ERROR: {e}")
        print("\n📌 Untuk Docker sandbox, install dengan:")
        print("   $ pip install 'openhands-sdk[docker]'")
        print("\n   Atau gunakan contoh standalone: python contoh_openhands.py")
        sys.exit(1)
    
    print("🚀 Inisialisasi OpenHands dengan Docker Sandbox...")
    print("📦 Agent akan berjalan di dalam container Docker\n")
    
    # Konfigurasi LLM
    llm = LLM(
        model='gpt-4o',
        api_key=api_key,
    )
    
    # Buat Docker sandbox
    sandbox = DockerSandbox()
    
    # Buat Agent dengan tools dari sandbox
    agent = Agent(
        llm=llm,
        tools=sandbox.get_tools(),
        description="AI Assistant dengan Docker sandbox"
    )
    
    # Buat conversation dengan workspace sandbox
    conversation = Conversation(
        agent=agent,
        workspace=sandbox.workspace
    )
    
    # Pesan tugas
    task = """
Tugas: 
1. Buat program Python sederhana 'kalkulator.py' yang:
   - Menerima 2 angka dari user
   - Melakukan operasi +, -, *, /
   - Menampilkan hasil
2. Jalankan program dengan input: 10, 5
3. Simpan output ke file 'hasil_kalkulasi.txt'
"""
    
    print("📝 Mengirim tugas ke OpenHands (Docker Sandbox)...\n")
    print("-" * 50)
    
    try:
        conversation.send_message(task)
        conversation.run()
        print("-" * 50)
        print("\n✅ Selesai!")
        print("\n📄 Files di sandbox:")
        print(f"   {sandbox.workspace}")
        
        # Cleanup
        sandbox.close()
        print("\n🧹 Docker sandbox ditutup")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Dihentikan oleh user")
        sandbox.close()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sandbox.close()
        sys.exit(1)

if __name__ == '__main__':
    main()
