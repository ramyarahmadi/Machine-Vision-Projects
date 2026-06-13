import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Configure the model
# max_num_hands=2 for detecting both hands
# min_detection_confidence=0.7 for stable tracking
model = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

print("Starting Hand Tracking... Press 'q' to exit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Error: Could not read from webcam.")
        break

    # Mirror the frame for natural interaction
    frame = cv2.flip(frame, 1)
    
    # MediaPipe requires RGB images, but OpenCV uses BGR
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame and find hands
    result = model.process(frame_rgb)

    # Draw landmarks if hands are detected
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow("Hand Tracking", frame)
    
    # Exit on 'q', 'e', 'ESC', or closing the window
    if cv2.waitKey(1) in [ord('q'), ord('e'), 27] or \
       cv2.getWindowProperty("Hand Tracking", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
