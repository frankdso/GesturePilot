import os

NIRCMD_PATH = "C:\\Users\\petle\\OneDrive\\Desktop\\Desktop\\Crazy\\GesturePilot\\nircmd.exe"

def volume_up():
    print("[ACTION] Volume Up")
    os.system(f'"{NIRCMD_PATH}" changesysvolume 5000')

def volume_down():
    print("[ACTION] Volume Down")
    os.system(f'"{NIRCMD_PATH}" changesysvolume -5000')
