#pip install opencv-python==4.12.0.88
import cv2

# Initialize the window
cv2.namedWindow("window", cv2.WINDOW_NORMAL)

# Access the webcam (0 is the default camera)
cap = cv2.VideoCapture(0)

print("Press 'q' or close the window to exit.")

while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        print("Failed to grab frame.")
        break
    
    # Flip the frame horizontally for a later mirror effect
    frame = cv2.flip(frame, 1)
    
    # Display the resulting frame
    cv2.imshow("window", frame)
    
    # Exit conditions: Pressing 'q' or closing the window manually
    if cv2.waitKey(1) == ord('q') or cv2.getWindowProperty("window", cv2.WND_PROP_VISIBLE) < 1:
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
