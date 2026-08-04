#!/usr/bin/env python3
"""
Workaround untuk error PlatformType
===================================
Import langsung dari file tanpa trigger broken module
"""

import sys
import os

# Block problematic imports
sys.modules['openhands.sdk.workspace'] = None

# Now import the cloud workspace
print("🔧 Applying workaround...")
print()

# Import openhands.workspace BEFORE anything else
import openhands.workspace
from openhands.workspace import OpenHandsCloudWorkspace
from openhands.sdk import Conversation

print("✅ Import workaround berhasil!")
print()

# Get API key
api_key = os.getenv('OPENHANDS_CLOUD_API_KEY')
if not api_key:
    print("❌ ERROR: OPENHANDS_CLOUD_API_KEY not set")
    print('   Set dengan: $env:OPENHANDS_CLOUD_API_KEY="sk-oh-..."')
    sys.exit(1)

print(f"🔑 API Key: {api_key[:15]}...")
print()

print("📦 Membuat Cloud Workspace...")
try:
    with OpenHandsCloudWorkspace(
        cloud_api_url="https://app.all-hands.dev",
        cloud_api_key=api_key,
    ) as workspace:
        print("✅ Cloud workspace berhasil dibuat!")
        print()
        
        # Test command
        result = workspace.execute_command("echo '🎉 WORKS!' && date")
        print(f"📨 Output:\n{result.stdout}")
        
        # Get LLM
        print("\n🔑 Mengambil LLM...")
        llm = workspace.get_llm()
        print(f"   Model: {llm.model}")
        
        # Make agent
        print("\n🤖 Membuat agent...")
        from openhands.tools.preset.default import get_default_agent
        agent = get_default_agent(llm=llm, cli_mode=True)
        
        # Conversation
        conversation = Conversation(agent=agent, workspace=workspace)
        
        # Send task
        print("\n📝 Mengirim tugas...")
        conversation.send_message("Buat file 'test.txt' yang berisi 'Berhasil!' dan tanggal")
        conversation.run()
        
        print("\n✅ Selesai!")
        
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
