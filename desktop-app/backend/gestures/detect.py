def detect_gesture(hand_landmarks, image_shape):
    h, w = image_shape
    tip_ids = [4, 8, 12, 16, 20]

    # Count folded fingers (skip thumb)
    folded_fingers = 0
    for tip_id in tip_ids[1:]:  # Index to Pinky
        tip = hand_landmarks.landmark[tip_id]
        base = hand_landmarks.landmark[tip_id - 2]
        if tip.y > base.y:
            folded_fingers += 1

    # Thumb logic
    thumb_tip = hand_landmarks.landmark[4]
    thumb_mcp = hand_landmarks.landmark[2]
    thumb_diff_y = thumb_tip.y - thumb_mcp.y

    if thumb_diff_y < -0.07:
        return "thumbs_up"
    elif thumb_diff_y > 0.07:
        return "thumbs_down"

    # Rock gesture (🤘) - index and pinky up
    if (
        hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and     # Index extended
        hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y and   # Pinky extended
        hand_landmarks.landmark[12].y > hand_landmarks.landmark[10].y and   # Middle folded
        hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y       # Ring folded
    ):
        return "rock"

    # Peace gesture (✌️) - index and middle extended, others folded
    if (
        hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and     # Index up
        hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y and   # Middle up
        hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y and   # Ring down
        hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y       # Pinky down
    ):
            return "peace"

    # Point right gesture (👉) — index up, others down, hand on left side
    if (
        hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and
        all(hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip - 2].y for tip in [12, 16, 20]) and
        hand_landmarks.landmark[0].x < 0.5
    ):
        return "point_right"

    # Point left gesture (👈) — index up, others down, hand on right side
    if (
        hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and
        all(hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip - 2].y for tip in [12, 16, 20]) and
        hand_landmarks.landmark[0].x > 0.5
    ):
        return "point_left"

    # Fist: All fingers folded
    if folded_fingers >= 4:
        return "fist"

    # Open hand: all up
    if folded_fingers == 0:
        return "open"
    
    thumb_tip = hand_landmarks.landmark[4]
    index_tip = hand_landmarks.landmark[8]
    thumb_index_dist = ((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2) ** 0.5

    if thumb_index_dist < 0.05:  # Tune as needed
        return "ok"

    return "none"
