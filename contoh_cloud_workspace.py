#!/usr/bin/env python3
"""
OpenHands Cloud Workspace - Contoh Lengkap
==========================================
Menggunakan OpenHands Cloud dengan SDK

API Key: sk-oh-... (OpenHands Cloud)
"""

import os
import sys

def main():
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY tidak ditemukan!")
        sys.exit(1)
    
    if not api_key.startswith('sk-oh-'):
        print("❌ ERROR: Butuh OpenHands Cloud API key (sk-oh-...)")
        print(f"   Key Anda: {api_key[:15]}...")
        sys.exit(1)
    
    print("=" * 60)
    print("🚀 OPENHANDS CLOUD WORKSPACE")
    print("=" * 60)
    print(f"API Key: {api_key[:15]}...\n")
    
    try:
        from openhands.sdk import Agent, Conversation
        from openhands.sdk.llm import LLM
        from openhands.sdk.workspace import CloudWorkspace
    except ImportError as e:
        print(f"❌ ERROR: {e}")
        print("   Install: pip install openhands-sdk openhands-tools")
        sys.exit(1)
    
    # ============================================================
    # METODE 1: Cloud Workspace dengan Managed LLM
    # ============================================================
    print("📦 Metode 1: Cloud Workspace (Managed LLM)")
    print("-" * 40)
    
    try:
        # Cloud workspace menggunakan LLM dari OpenHands Cloud
        workspace = CloudWorkspace(
            api_key=api_key,
            # workspace_id='your-workspace-id'  # Opsional
        )
        
        # Agent dengan tools dari workspace
        agent = Agent(
            llm=workspace.get_llm(),  # Gunakan LLM dari cloud
            tools=workspace.get_tools(),
        )
        
        conversation = Conversation(
            agent=agent,
            workspace=workspace
        )
        
        print("✓ Cloud workspace configured")
        print(f"  Workspace: {workspace}")
        
        # Cleanup
        workspace.close()
        
    except Exception as e:
        print(f"⚠️ CloudWorkspace not available: {e}")
        print("   Trying alternative method...\n")
    
    # ============================================================
    # METODE 2: Remote Agent Server (Recommended)
    # ============================================================
    print("\n📡 Metode 2: Remote Agent Server")
    print("-" * 40)
    print("""
Untuk menggunakan OpenHands Cloud dengan cara terbaik:

1. Jalankan CLI OpenHands:
   $ openhands --api-key $OPENAI_API_KEY

2. Atau gunakan agent-server mode:
   $ openhands-server --api-key $OPENAI_API_KEY --port 3000

3. Hubungkan SDK ke server:
""")
    
    # Contoh kode untuk connect ke local server
    print("""
#---- contoh_connect.py ----
from openhands.sdk import Agent, Conversation

# Connect ke local/remote agent server
agent_server_url = "http://localhost:3000"  # Atau URL cloud Anda

conversation = Conversation.start(
    base_url=agent_server_url,
    api_key=os.getenv('OPENAI_API_KEY'),
)

conversation.send_message("Tugas Anda di sini")
conversation.run()
#----------------------------
""")
    
    # ============================================================
    # METODE 3: Langsung dengan LLM (tanpa cloud)
    # ============================================================
    print("\n🔧 Metode 3: Langsung SDK (butuh LLM API key)")
    print("-" * 40)
    print("""
Jika Anda ingin coba langsung tapi butuh OpenAI API key:

# Set kedua API key
export OPENAI_API_KEY='sk-...'       # OpenAI untuk LLM
export OPENHANDS_API_KEY='sk-oh-...'  # OpenHands Cloud

# Atau gunakan script contoh_openhands.py dengan OpenAI key
""")
    
    print("\n" + "=" * 60)
    print("📋 RINGKASAN")
    print("=" * 60)
    print("""
UNTUK MENGGUNAKAN OPENHANDS CLOUD ANDA:

Option A: CLI Interaktif
   $ openhands --api-key $OPENAI_API_KEY
   
Option B: Browser UI
   $ openhands --ui --api-key $OPENAI_API_KEY
   # Buka http://localhost:3000

Option C: SDK dengan Remote Server
   1. Jalankan server: openhands-server --api-key $OPENAI_API_KEY
   2. Connect dari SDK ke server tersebut

Option D: Managed LLM dari Cloud
   Gunakan CloudWorkspace jika workspace Anda dikonfigurasi
   dengan LLM credentials

📚 Dokumentasi: docs.openhands.dev
🌐 Dashboard: app.all-hands.dev
""")

if __name__ == '__main__':
    main()
