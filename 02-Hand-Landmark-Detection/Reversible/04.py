import cv2
import mediapipe

mypen = mediapipe.solutions.drawing_utils
mp_hand = mediapipe.solutions.hands
mymodel = mp_hand.Hands(max_num_hands=1,min_detection_confidence=0.7)
CAP = cv2.VideoCapture(0)
cv2.namedWindow('w_1',cv2.WINDOW_NORMAL)
while CAP.isOpened():
    ret, frame = CAP.read()
    if not ret:
        break
    frame = cv2.flip(frame,1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mymodel.process(frame_rgb)
    if result.multi_hand_landmarks :
        for i,j in zip(result.multi_hand_landmarks,result.multi_handedness):
            mypen.draw_landmarks(frame, i, mp_hand.HAND_CONNECTIONS)
            Which_hand = j.classification[0].label
            score = j.classification[0].score
            label = j.classification[0].label
            index= j.classification[0].index
            print(f'score:{score},label:{label},index:{index}')

            landmarks = i.landmark
            print(f'landmarks[4].x - landmarks[0].x: {landmarks[4].x - landmarks[0].x}')
            print(f'landmarks[0].x - landmarks[4].x: {landmarks[0].x - landmarks[4].x}')

            fingers=[False]*5
            if Which_hand == 'Right':
                if landmarks[0].x - landmarks[4].x > 0.1  or  landmarks[4].x - landmarks[0].x > 0.1 :
                    fingers[0] = True

            else:
                if landmarks[0].x - landmarks[4].x > 0.1  or  landmarks[4].x - landmarks[0].x > 0.1 :
                        fingers[0] = True

            for z in range(1, 5):
                if landmarks[0].y > landmarks[z].y :
                    if landmarks[(4 * z) + 4].y < landmarks[(4 * z) + 2].y:
                        fingers[z] = True
                else:
                    if landmarks[(4 * z) + 4].y > landmarks[(4 * z) + 2].y:
                        fingers[z] = True

            javab = fingers.count(True)
            cv2.putText(frame,f"number:{javab}",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow('w_1',frame)
    if cv2.waitKey(1) == ord('q') or cv2.getWindowProperty('w_1',cv2.WND_PROP_VISIBLE) < 1:
        break
CAP.release()
cv2.destroyAllWindows()
