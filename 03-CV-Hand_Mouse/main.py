import mediapipe
import cv2
import pyautogui

w , h = pyautogui.size()


cap = cv2.VideoCapture(0)
mp_hand = mediapipe.solutions.hands
mp_drawing = mediapipe.solutions.drawing_utils
model  = mp_hand.Hands(min_detection_confidence=0.7)

while cap.isOpened():
    m , f  = cap.read()
    if not m :
        break
    f = cv2.flip(f,1)
    f_rgb = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
    result = model.process(f_rgb)
    if result.multi_hand_landmarks :
        for dm , dinfo in zip(result.multi_hand_landmarks,result.multi_handedness):
            mp_drawing.draw_landmarks(f,dm,mp_hand.HAND_CONNECTIONS)
            landmarks = dm.landmark
            x = int(landmarks[8].x * w)
            y = int(landmarks[8].y * h)
            pyautogui.moveTo(x,y)
    cv2.imshow("Result", f)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
