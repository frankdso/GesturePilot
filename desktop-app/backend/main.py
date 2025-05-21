import sys
import os

# Add backend directory and its subfolders to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, 'gestures'))
sys.path.append(os.path.join(current_dir, 'actions'))

import cv2
import mediapipe as mp
from gestures.detect import detect_gesture
from actions.volume import volume_up, volume_down
from actions.focus import trigger_focus_mode
from actions.spotify import toggle_play_pause, next_song
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from actions.screenshot import take_screenshot
from gestures.slider_tracker import BrightnessTracker
from actions.brightness import change_brightness

# from gestures.swipe_tracker import SwipeTracker
# from actions.window import (
#     start_window_switching,
#     cycle_window,
#     confirm_window_selection,
#     _alt_held
# )


scope = "user-read-playback-state user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="e4f7301f424d47d6b7bcd97c7ffabc9c",
        client_secret="8cf93e600d8a4e8581605c7f409a5c54",
        redirect_uri="http://127.0.0.1:8888/callback",
        scope=scope
    ))


# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
last_trigger_time = 0
cooldown_seconds = 5
last_play_pause = 0
current_action = ""
last_screenshot = 0
brightness_tracker = BrightnessTracker()

# Open webcam
cap = cv2.VideoCapture(0)

# swipe_tracker = SwipeTracker()

print("[INFO] Starting camera... Press 'q' to quit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip and convert to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process with MediaPipe
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks on frame
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = detect_gesture(hand_landmarks, frame.shape[:2])
            print(f"[DEBUG] Gesture: {gesture}")
            # Bottom-left box display
            h, w, _ = frame.shape
            cv2.rectangle(frame, (10, h - 80), (300, h - 10), (0, 0, 0), -1)  # Background box

            cv2.putText(frame, f"Gesture: {gesture}", (20, h - 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            cv2.putText(frame, f"Action: {current_action}", (20, h - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 255), 2)

            if gesture == "thumbs_up":
                volume_up()
                current_action = "Volume Up"
            if gesture == "thumbs_down":
                volume_down()
                current_action = "Volume Down"
            if gesture == "point_right" and brightness_tracker.should_trigger("right"):
                change_brightness(10)
                current_action = "Brightness Up"
            if gesture == "point_left" and brightness_tracker.should_trigger("left"):
                change_brightness(-10)
                current_action = "Brightness Down"

            if gesture == "ok" and time.time() - last_screenshot > 5:
                  take_screenshot()
                  current_action = "Screenshot Taken"
                  last_screenshot = time.time()
            
            for idx, lm in enumerate(hand_landmarks.landmark):
                h, w, _ = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(f"Landmark {idx}: ({cx}, {cy})")

    # Show frame
    cv2.imshow("GesturePilot - Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

