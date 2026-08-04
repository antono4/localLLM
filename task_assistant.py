#!/usr/bin/env python3
"""
🤖 AI Task Assistant - Local LLM Edition
==========================================
Aplikasi Otomasi Tugas dengan OpenHands Cloud

Gunakan API key OpenHands Cloud untuk menjalankan berbagai tugas
otomatis dengan bantuan AI.

Usage:
    export OPENHANDS_CLOUD_API_KEY='sk-oh-your-key'
    python task_assistant.py
    
Author: AI Assistant (OpenHands)
Repository: https://github.com/antono4/localLLM
"""

import os
import sys
from typing import Optional, Dict, Any, Callable

# ANSI color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_banner():
    """Print application banner"""
    banner = f"""
{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   {Colors.BOLD}🤖 AI TASK ASSISTANT - Local LLM Edition{Colors.ENDC}{Colors.CYAN}           ║
║                                                           ║
║   Automate your tasks with OpenHands Cloud AI             ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝{Colors.ENDC}
    """
    print(banner)

def print_success(msg: str):
    print(f"{Colors.GREEN}✓ {msg}{Colors.ENDC}")

def print_error(msg: str):
    print(f"{Colors.RED}✗ {msg}{Colors.ENDC}")

def print_info(msg: str):
    print(f"{Colors.BLUE}ℹ {msg}{Colors.ENDC}")

def print_warning(msg: str):
    print(f"{Colors.YELLOW}⚠ {msg}{Colors.ENDC}")

class TaskAssistant:
    """AI Task Assistant using OpenHands Cloud"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('OPENHANDS_CLOUD_API_KEY')
        self.workspace = None
        self.agent = None
        self.llm = None
        
        if not self.api_key:
            raise ValueError(
                f"{Colors.RED}ERROR: OpenHands Cloud API key tidak ditemukan!{Colors.ENDC}\n"
                f"\nSet dengan:\n"
                f"  export OPENHANDS_CLOUD_API_KEY='sk-oh-...'\n"
                f"\nDapatkan API key di: https://app.all-hands.dev"
            )
    
    def connect(self) -> bool:
        """Connect to OpenHands Cloud"""
        try:
            print_info("Menghubungkan ke OpenHands Cloud...")
            
            from openhands.workspace.cloud import OpenHandsCloudWorkspace
            from openhands.tools.preset.default import get_default_agent
            from openhands.sdk import Conversation
            
            self.workspace = OpenHandsCloudWorkspace(
                cloud_api_url="https://app.all-hands.dev",
                cloud_api_key=self.api_key,
            )
            
            # Initialize workspace
            self.workspace.__enter__()
            
            # Get managed LLM from cloud
            self.llm = self.workspace.get_llm()
            
            # Create agent
            self.agent = get_default_agent(llm=self.llm, cli_mode=True)
            
            print_success("Berhasil terhubung ke OpenHands Cloud!")
            print_info(f"LLM: {self.llm.model}")
            
            return True
            
        except ImportError as e:
            print_error(f"Package tidak ditemukan: {e}")
            print_info("Install dengan: pip install openhands-sdk openhands-tools openhands-workspace")
            return False
        except Exception as e:
            print_error(f"Gagal terhubung: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from OpenHands Cloud"""
        if self.workspace:
            try:
                self.workspace.__exit__(None, None, None)
                print_info("Koneksi ditutup")
            except:
                pass
    
    def execute_task(self, task: str, workspace_path: Optional[str] = None) -> bool:
        """Execute a task using OpenHands Cloud"""
        if not self.agent or not self.workspace:
            print_error("Belum terhubung ke OpenHands Cloud. Jalankan connect() terlebih dahulu.")
            return False
        
        try:
            from openhands.sdk import Conversation
            
            workspace_dir = workspace_path or os.getcwd()
            
            print_info(f"Workspace: {workspace_dir}")
            print_info("Menjalankan task...")
            print("-" * 60)
            
            conversation = Conversation(
                agent=self.agent,
                workspace=self.workspace
            )
            
            conversation.send_message(task)
            conversation.run()
            
            print("-" * 60)
            print_success("Task selesai!")
            return True
            
        except Exception as e:
            print_error(f"Error menjalankan task: {e}")
            return False
    
    def run_preset_task(self, task_type: str) -> bool:
        """Run a preset task"""
        preset_tasks = {
            "hello": "Buat file hello.txt yang berisi 'Hello from AI Task Assistant!' dan tanggal saat ini",
            "readme": "Buat file README.md untuk project ini dengan format yang bagus, berisi deskripsi, instalasi, dan usage",
            "backup": "Buat backup semua file .py di folder saat ini ke folder backup/",
            "analyze": "Analisis semua file .py di folder saat ini dan buat laporan tentang struktur code",
            "clean": "Hapus semua file temporary (.pyc, __pycache__, .gitignore) dan buat .gitignore yang proper",
            "test": "Buat unit test untuk semua function di file main.py (jika ada)",
            "docs": "Tambahkan docstring dan comments ke semua function di file main.py (jika ada)",
            "security": "Scan semua file .py untuk potensi security issues dan buat laporan",
        }
        
        if task_type not in preset_tasks:
            print_error(f"Task '{task_type}' tidak dikenal")
            print_info(f"Task yang tersedia: {', '.join(preset_tasks.keys())}")
            return False
        
        print_info(f"Menjalankan preset task: {task_type}")
        return self.execute_task(preset_tasks[task_type])


def show_help():
    """Show help message"""
    help_text = f"""
{Colors.CYAN}📖 PETUNJUK PENGGUNAAN{Colors.ENDC}

{Colors.BOLD}Setup:{Colors.ENDC}
    export OPENHANDS_CLOUD_API_KEY='sk-oh-...'
    python task_assistant.py

{Colors.BOLD}Preset Tasks:{Colors.ENDC}
    python task_assistant.py --task hello
    python task_assistant.py --task readme
    python task_assistant.py --task backup
    python task_assistant.py --task analyze
    python task_assistant.py --task clean
    python task_assistant.py --task test
    python task_assistant.py --task docs
    python task_assistant.py --task security

{Colors.BOLD}Custom Task:{Colors.ENDC}
    python task_assistant.py --custom "Buat file app.py dengan Flask app sederhana"

{Colors.BOLD}Interactive Mode:{Colors.ENDC}
    python task_assistant.py --interactive

{Colors.BOLD}Examples:{Colors.ENDC}
    # Buat file hello
    python task_assistant.py --task hello
    
    # Analisis code
    python task_assistant.py --task analyze
    
    # Custom task
    python task_assistant.py --custom "Buat program CLI untuk manage todo list"
    
    # Interactive mode
    python task_assistant.py --interactive
"""
    print(help_text)


def interactive_mode(assistant: TaskAssistant):
    """Run in interactive mode"""
    print(f"\n{Colors.GREEN}🎯 Interactive Mode{Colors.ENDC}")
    print("Ketik 'help' untuk bantuan, 'exit' untuk keluar\n")
    
    while True:
        try:
            task = input(f"{Colors.CYAN}Task>{Colors.ENDC} ").strip()
            
            if not task:
                continue
            
            if task.lower() in ['exit', 'quit', 'q']:
                print("Sampai jumpa! 👋")
                break
            
            if task.lower() == 'help':
                show_help()
                continue
            
            print()
            assistant.execute_task(task)
            print()
            
        except KeyboardInterrupt:
            print("\n\nSampai jumpa! 👋")
            break


def main():
    """Main entry point"""
    print_banner()
    
    # Parse arguments
    import argparse
    
    parser = argparse.ArgumentParser(
        description='🤖 AI Task Assistant - Automate tasks with OpenHands Cloud',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--task', '-t',
        choices=['hello', 'readme', 'backup', 'analyze', 'clean', 'test', 'docs', 'security'],
        help='Preset task to run'
    )
    parser.add_argument(
        '--custom', '-c',
        help='Custom task description'
    )
    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Run in interactive mode'
    )
    parser.add_argument(
        '--api-key',
        help='OpenHands Cloud API key (or set OPENHANDS_CLOUD_API_KEY env var)'
    )
    
    args = parser.parse_args()
    
    # Get API key
    api_key = args.api_key or os.getenv('OPENHANDS_CLOUD_API_KEY')
    
    if not api_key:
        print_error("OpenHands Cloud API key tidak ditemukan!")
        print(f"\n{Colors.YELLOW}Dapatkan API key di: https://app.all-hands.dev{Colors.ENDC}")
        print(f"\nAtau set dengan:\n  export OPENHANDS_CLOUD_API_KEY='sk-oh-...'")
        show_help()
        sys.exit(1)
    
    # Create assistant
    try:
        assistant = TaskAssistant(api_key=api_key)
    except ValueError as e:
        print(e)
        sys.exit(1)
    
    # Connect
    if not assistant.connect():
        sys.exit(1)
    
    try:
        # Determine what to run
        if args.interactive:
            interactive_mode(assistant)
        elif args.task:
            assistant.run_preset_task(args.task)
        elif args.custom:
            assistant.execute_task(args.custom)
        else:
            # Default: show help
            show_help()
    finally:
        assistant.disconnect()


if __name__ == '__main__':
    main()
