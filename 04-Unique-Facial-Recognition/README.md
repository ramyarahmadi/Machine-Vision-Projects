# 🎯 Face Recognition with OpenCV and Python

This project uses face recognition with a webcam to detect and identify faces in real time.

The program loads a reference image, encodes the face, then compares it with faces seen by the webcam.

If a match is found, the person’s name is displayed on the video frame.
Features

    Real-time face detection from webcam
    Face encoding and comparison using face_recognition
    Drawing a rectangle around detected faces
    Displaying the recognized person’s name
    Simple and easy-to-understand Python code

# How It Works  🧠

    A reference image is loaded from disk.
    The face in that image is encoded.
    The webcam captures live video frames.
    Each frame is converted to RGB.
    Faces in the frame are detected and encoded.
    The encodings are compared with the known face encodings.
    If the similarity is high enough, the person’s name is shown on the screen.

Technologies Used

    Python
    OpenCV
    face_recognition
    NumPy
    dlib(match with your python version download it on github after that use pip install)

Installation on Windows

    Important:

    On Windows, dlib must be installed first, because face_recognition depends on it.

Step 1: Install the precompiled dlib wheel

Before installing face_recognition, you should install the compiled dlib package for Windows.

Example:

                                                                    bash
pip install dlib‑<version>‑cp<python-version>‑cp<python-version>‑win_amd64.whl

If you are using a ready-made wheel file, install it directly from the terminal:

                                                                    bash
pip install dlib-19.24.2-cp310-cp310-win_amd64.whl

    Make sure the wheel version matches your Python version.

Step 2: Install face_recognition

After dlib is installed successfully, install the face recognition library:

                                                                    bash
pip install face_recognition

Step 3: Install other dependencies

                                                                    bash
pip install opencv-python numpy

Usage

Run the script:

                                                                    bash
python main.py

    Press q to quit the webcam window.

Project Structure

                                                                    bash
project-folder/
│
├── ramyar.jpg
├── main.py
└── README.md

Notes

    The webcam must be connected and accessible.
    If no face is detected in the reference image, the code may raise an error.
    You can add more reference images by encoding more faces and placing them in the faceha_encodeshode list.

Example Code Idea

This project demonstrates:

    loading an image,
    encoding faces,
    detecting faces from live webcam,
    comparing encodings,
    and labeling recognized faces in real time.

License

This project is open-source and free to use for educational purposes.
