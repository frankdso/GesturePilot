import pyautogui
import os
from datetime import datetime

def take_screenshot():
    screenshot_dir = os.path.join(os.environ['USERPROFILE'], 'Pictures', 'GesturePilotScreenshots')
    os.makedirs(screenshot_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(screenshot_dir, f'screenshot_{timestamp}.png')

    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)

    print(f"[ACTION] Screenshot saved to {filepath}")
