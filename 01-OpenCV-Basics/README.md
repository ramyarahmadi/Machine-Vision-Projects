01 - OpenCV Basics: Webcam Feed 📸

This is the introductory project of my Machine Vision series. It focuses on the fundamental implementation of a real-time video stream using the OpenCV library.

🚀 Key Features
- **Real-time Capture:** Accesses the default system webcam.
- **Frame Manipulation:** Implements a horizontal flip (`cv2.flip`) to create a natural mirror effect for the user.
- **Smart Window Management:** The script detects if the window is closed manually by the user or if the 'q' key is pressed, ensuring a clean exit without hanging processes.

🛠️ Technical Details
The script uses a `while` loop to continuously read frames from the `VideoCapture` object. It ensures that memory is properly released using `cap.release()` and `cv2.destroyAllWindows()` once the loop terminates.

Prerequisites
To run this project, ensure you have Python installed and install the necessary library:
```bash
pip install opencv-python==4.12.0.88


🧠 What I Learned

    Managing video streams and frame-by-frame processing.
    Handling user input and window events in OpenCV.
    The importance of “Mirroring” in human-computer interaction (HCI).
