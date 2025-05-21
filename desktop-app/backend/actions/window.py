# import pyautogui

# _alt_held = False  # Global state flag

# def start_window_switching():
#     global _alt_held
#     if not _alt_held:
#         pyautogui.keyDown('alt')
#         pyautogui.press('tab')
#         _alt_held = True
#         print("[ACTION] Alt held + first window selected")

# def cycle_window(direction="right"):
#     if _alt_held:
#         if direction == "right":
#             pyautogui.press('tab')
#             print("[ACTION] Switched to next window")
#         elif direction == "left":
#             pyautogui.keyDown('shift')
#             pyautogui.press('tab')
#             pyautogui.keyUp('shift')
#             print("[ACTION] Switched to previous window")

# def confirm_window_selection():
#     global _alt_held
#     if _alt_held:
#         pyautogui.keyUp('alt')
#         _alt_held = False
#         print("[ACTION] Confirmed window selection (Alt released)")
