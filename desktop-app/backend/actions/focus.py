import os
import subprocess
import threading
from .spotify import play_spotify

def open_vscode():
    print("[ACTION] Launching VS Code...")
    # try:
    #     subprocess.Popen(["cmd", "/c", "start", "", r"C:\Users\petle\OneDrive\Desktop\Desktop\Other Apps\Visual Studio Code.lnk"])
    # except Exception as e:
    #     print("[ERROR] Could not open VS Code:", e)

def trigger_focus_mode():
    # Run both actions in parallel
    threading.Thread(target=open_vscode).start()
    threading.Thread(target=play_spotify).start()
