import screen_brightness_control as sbc

def change_brightness(delta):
    try:
        current = sbc.get_brightness(display=0)[0]
        new_level = max(0, min(100, current + delta))
        sbc.set_brightness(new_level, display=0)
        print(f"[ACTION] Brightness set to {new_level}%")
    except Exception as e:
        print(f"[ERROR] Brightness change failed: {e}")
