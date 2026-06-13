02 - Hand Landmark Detection 🖐️

This project implements real-time hand tracking and landmark detection using Google's **MediaPipe** framework and **OpenCV**.

🌟 Features
- **Dual Hand Tracking:** Capable of detecting and tracking up to 2 hands simultaneously.
- **21-Point Landmark Model:** Visualizes all finger joints and palm structures.
- **Robust Detection:** Uses a 70% confidence threshold to reduce flickering and false positives.

🛠️ Tech Stack
- **Python**
- **MediaPipe:** For the machine learning pipeline.
- **OpenCV:** For video stream handling and visualization.

🚀 Installation
```bash
pip install opencv-python mediapipe==0.10.14


🧠 Core Concept
The pipeline of this project works as follows:

1. The webcam captures frames using OpenCV in **BGR format**.
2. Frames are converted to **RGB**, which is required by MediaPipe.
3. The MediaPipe Hands model processes the frame and detects **21 hand landmarks**.
4. The detected landmarks are mapped back onto the original video frame.
5. MediaPipe drawing utilities are used to visualize the hand skeleton and connections in real time.
