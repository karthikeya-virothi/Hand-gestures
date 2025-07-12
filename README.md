# ✋ Gesture Control Using Hand Recognition (Python + OpenCV + MediaPipe)

A Python-based hand gesture recognition app that allows you to control your system (keyboard presses) using simple finger gestures via webcam. It uses **MediaPipe** for real-time hand tracking and **PyAutoGUI** for simulating keypresses.

---

## 📽️ Demo
- ✌️ Two fingers up = `left` key
- 👉 One finger (index) up = `up` key
- ✊ Fist (no fingers up) = `down` key
- 🖐️ All four fingers up = `right` key

These simulate arrow key presses in any active application (e.g., games, slides, etc.).

---

## 🛠️ Requirements

Install dependencies with:

```bash
pip install opencv-python mediapipe pyautogui
```

Python 3.7 or later is recommended.

---

## 📁 Project Files

- `gesture_control.py` – Main script that runs the gesture control
- No other files required; runs directly using webcam

---

## 🚀 How to Run

1. Connect your webcam.
2. Run the script:

```bash
python gesture_control.py
```

3. A window will open. Use your hand gestures in front of the webcam.
4. Press `q` to quit.

---

## 🧠 How It Works

- Uses **MediaPipe Hands** to detect hand landmarks.
- Tracks finger positions to identify which fingers are raised.
- Maps specific finger combinations to gestures.
- Simulates keyboard arrow key presses using **PyAutoGUI**.
- Optional: Displays FPS in console.

---

## 💡 Gesture Mappings

| Gesture                        | Keys Triggered  |
|--------------------------------|-----------------|
| Index finger up               | `up` arrow key  |
| All fingers down (fist)       | `down` arrow key|
| Index + middle finger up      | `left` arrow key|
| All 4 fingers (no thumb) up   | `right` arrow key|

---

## 🔒 Notes & Tips

- Runs best under good lighting.
- Keep only one hand visible to avoid confusion.
- Works on Windows, Linux, and macOS.
- You can change the gesture → key mapping easily in the code.

---

## 🧑‍💻 Author

Developed by [Your Name].  
Feel free to modify or enhance this code for personal or academic use.

---

## 📜 License

MIT License – free to use, share, and modify.
