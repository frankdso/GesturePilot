# from collections import deque

# class SwipeTracker:
#     def __init__(self, buffer_len=5, threshold=60):
#         self.wrist_x_history = deque(maxlen=buffer_len)
#         self.trigger_threshold = threshold  # pixels to count as a swipe

#     def update(self, wrist_x_pixel):
#         self.wrist_x_history.append(wrist_x_pixel)

#         if len(self.wrist_x_history) < self.wrist_x_history.maxlen:
#             return None  # Not enough data yet

#         delta = self.wrist_x_history[-1] - self.wrist_x_history[0]

#         if delta > self.trigger_threshold:
#             self.wrist_x_history.clear()
#             return "swipe_right"
#         elif delta < -self.trigger_threshold:
#             self.wrist_x_history.clear()
#             return "swipe_left"
#         return None
