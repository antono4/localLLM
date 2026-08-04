#!/usr/bin/env python3
"""
Contoh OpenHands SDK - Hello World
===================================
Script ini mendemonstrasikan cara menggunakan OpenHands SDK 
untuk membuat AI agent yang dapat mengerjakan tugas pemrograman.

Sebelum menjalankan:
1. Set API key: export OPENAI_API_KEY='sk-...'
2. Atau edit baris di bawah dengan API key Anda
"""

import os
import sys

# ============================================================
# KONFIGURASI - Ganti sesuai kebutuhan Anda
# ============================================================

# Opsi 1: Set environment variable
# export OPENAI_API_KEY='sk-your-key-here'

# Opsi 2: Masukkan API key langsung (tidak direkomendasikan untuk production)
# API_KEY = 'sk-your-key-here'

# Opsi 3: Menggunakan Anthropic Claude
# MODEL = 'claude-sonnet-4-20250514'
# BASE_URL = 'https://api.anthropic.com'
# API_KEY = os.getenv('ANTHROPIC_API_KEY')

# ============================================================
# SCRIPT UTAMA
# ============================================================

def main():
    # Cek API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY tidak ditemukan!")
        print("\n📌 Untuk menjalankan script ini:")
        print("   Option 1: Set environment variable")
        print("   $ export OPENAI_API_KEY='sk-your-key-here'")
        print("   $ python contoh_openhands.py")
        print()
        print("   Option 2: Edit script dan masukkan API key langsung")
        print()
        print("📚 Baca OPENHANDS_LOKAL.md untuk panduan lengkap")
        sys.exit(1)
    
    try:
        from openhands.sdk import LLM, Agent, Conversation
        from openhands.tools.terminal import TerminalTool
        from openhands.tools.file_editor import FileEditorTool
    except ImportError as e:
        print(f"❌ ERROR: Gagal import OpenHands SDK: {e}")
        print("\n📌 Instalasi:")
        print("   $ pip install openhands-sdk openhands-tools")
        sys.exit(1)
    
    print("🚀 Inisialisasi OpenHands...")
    
    # Konfigurasi LLM
    llm = LLM(
        model='gpt-4o',  # Model yang digunakan
        api_key=api_key,
    )
    
    # Buat Agent dengan tools yang diperlukan
    agent = Agent(
        llm=llm,
        tools=[
            TerminalTool,   # Menjalankan perintah terminal
            FileEditorTool, # Membaca/menulis file
        ],
        description="AI Assistant yang membantu programming"
    )
    
    # Folder kerja
    workspace = os.getcwd()
    print(f"📁 Workspace: {workspace}")
    
    # Buat conversation
    conversation = Conversation(
        agent=agent,
        workspace=workspace
    )
    
    # Pesan tugas
    task = """
Tugas: Buat file 'hello_openhands.txt' yang berisi:
1. Sapaan "Hello dari OpenHands!"
2. Tanggal dan waktu pembuatan
3. 2 fakta menarik tentang Python
"""
    
    print("\n📝 Mengirim tugas ke OpenHands...\n")
    print("-" * 50)
    
    # Kirim dan jalankan
    conversation.send_message(task)
    conversation.run()
    
    print("-" * 50)
    print("\n✅ Selesai!")
    print("\n📄 Cek file 'hello_openhands.txt' di folder kerja Anda")

if __name__ == '__main__':
    main()
