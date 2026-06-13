## 🔄 Handling Hand Symmetry (The Mirroring Problem)

One of the key challenges in hand tracking is the **Mirroing Effect**. When the webcam frame is flipped for a natural user experience (`cv2.flip(frame, 1)`), the spatial orientation of the hand changes.

### ⚠️ The Challenge
In a mirrored frame, MediaPipe might misinterpret a **Right Hand** as a **Left Hand**, or vice versa. This leads to logic errors when detecting the **Thumb**, because the thumb's "open" position depends on whether it's the left or right hand (comparing X-coordinates).

### 🛠️ The Solution
To solve this, we implemented a **Multi-Handedness Logic**:

1. **Classification Access:** We use `result.multi_handedness` to get the real-time label of the hand (`Left` or `Right`).
2. **Conditional Logic:** 
   - For the **Left Hand**: The thumb is considered open if its tip (Landmark 4) is to the *right* of its base.
   - For the **Right Hand**: The thumb is considered open if its tip is to the *left* of its base.
3. **Dynamic Comparison:** This ensures that no matter how the camera is oriented or which hand is use, the finger count remains 100% accurate.

### 🧮 Inversion-Proof Logic
Beyond symmetry, we also solved the **Inversion Problem** (when the hand is upside down). Instead of using absolute Y-coordinates (Up/Down), we calculate the **Euclidean Distance** between the fingertips and the wrist:
- If `Distance(Tip, Wrist > Distance(Joint, Wrist)`, the finger is **Open**.
- This makes the algorithm work at any angle (360° rotation).
