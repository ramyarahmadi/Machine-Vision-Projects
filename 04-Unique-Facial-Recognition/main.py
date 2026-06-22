import face_recognition
import cv2
import numpy as np

pic_ramyar=face_recognition.load_image_file('ramyar.jpg')
#pic_parinaz=face_recognition.load_image_file('parinaz.jpeg')
#pic_dalia=face_recognition.load_image_file('dalia.png')

pic_encode_ramyar=face_recognition.face_encodings(pic_ramyar)[0]
#pic_encode_parinaz=face_recognition.face_encodings(pic_parinaz)[0]
#pic_encode_dalia=face_recognition.face_encodings(pic_dalia)[0]
#لیست چهره های انکد شده
faceha_encodeshode=[pic_encode_ramyar]#pic_parinaz,pic_encode_dalia]

face_names=['ramyar','parinaz','dalia']
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame,1)
    rgb_f = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_f)   #چهره های انسان ها کجاست؟ در وبکم
    face_encodings = face_recognition.face_encodings(rgb_f, face_locations) #انکود چهره ها در مکان وبکم
    #دسترسی به مکان چهره ها برای رسم مستطیل جهت شناسایی و دسنررسی به انکود چهره ها برای مقایسه
    for (y1,x1,y2,x2), encode_face in zip(face_locations,face_encodings):
        #  مقایسه چهره های انکود شده در وب کم و در تصویر داده شده که نتیجه ترو و فالس است
        matches = face_recognition.compare_faces(faceha_encodeshode,encode_face,tolerance=0.6)
        name = "unknown"
        #محاسبه فاصله چهره انکود شده وب کم با چهره درون تصویر
        face_dist = face_recognition.face_distance(faceha_encodeshode,encode_face)
        # بهترین فاصله یعنی بیشترین شباهت و یعنی حداقل تفاوت یا فاصله
        best_match_index = np.argmin(face_dist)
        # اگر شخصیت درون وبکم با چهره درون عکس ترو شده و با اندیس کمترین فاصله ترو شده
        if matches[best_match_index]:
            name = face_names[best_match_index]
        #رسم مستطیل دور چهره
        cv2.rectangle(frame,(x1,y1),(x2,y2),(100,200,44),2)
        cv2.putText(frame,name,(x1,y1),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow('تشخیص چهره',frame)
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty("تشخیص چهره",cv2.WND_PROP_VISIBLE) < 1  :
        break
cap.release()
cv2.destroyAllWindows()
