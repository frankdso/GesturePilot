# gestures/slider_tracker.py
import time

class BrightnessTracker:
    def __init__(self):
        self.last_trigger_time = {
            "left": 0,
            "right": 0
        }
        self.cooldown = 1.0  # seconds

    def should_trigger(self, direction: str) -> bool:
        now = time.time()
        if direction not in self.last_trigger_time:
            return False

        if now - self.last_trigger_time[direction] > self.cooldown:
            self.last_trigger_time[direction] = now
            return True

        return False
