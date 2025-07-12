import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,  # Limit to one hand for speed
    min_detection_confidence=0.7,
    min_tracking_confidence=0.6
)
mp_draw = mp.solutions.drawing_utils

# Start webcam and set resolution
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Gesture tracking
prev_gesture = None
last_action_time = 0
gesture_delay = 0.8  # seconds between actions

# FPS tracking
start_time = time.time()
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror view
    h, w, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    current_gesture = None

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            landmarks = hand_landmarks.landmark

            # Check if fingers are up
            index_finger_up = landmarks[8].y < landmarks[6].y
            middle_finger_up = landmarks[12].y < landmarks[10].y
            ring_finger_up = landmarks[16].y < landmarks[14].y
            pinky_finger_up = landmarks[20].y < landmarks[18].y

            open_fingers = sum([index_finger_up, middle_finger_up, ring_finger_up, pinky_finger_up])

            # Determine gesture
            if open_fingers == 1 and index_finger_up:
                current_gesture = "up"
            elif open_fingers == 0:
                current_gesture = "down"
            elif open_fingers == 4:
                current_gesture = "right"
            elif open_fingers == 2 and index_finger_up and middle_finger_up:
                current_gesture = "left"

            # Trigger key only if gesture changed and delay passed
            if current_gesture != prev_gesture and time.time() - last_action_time > gesture_delay:
                if current_gesture:
                    pyautogui.press(current_gesture)
                    print(f"Gesture: {current_gesture}")
                    prev_gesture = current_gesture
                    last_action_time = time.time()

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Show FPS (optional for debugging)
    frame_count += 1
    if frame_count >= 10:
        fps = frame_count / (time.time() - start_time)
        print("FPS:", round(fps, 2))
        frame_count = 0
        start_time = time.time()

    # Display frame
    cv2.imshow("Hand Gesture Control", frame)

    # Exit key
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
