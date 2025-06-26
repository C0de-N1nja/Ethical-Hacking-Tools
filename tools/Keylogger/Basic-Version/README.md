# 📄 Basic Python Keylogger

This script demonstrates a simple keylogger built in Python using the `pynput` library. It captures all keystrokes from the user's keyboard and logs them to a local file. Designed for beginners and cybersecurity students, it provides a foundational understanding of how keyloggers operate.

---

## 🔧 Features

- Records all keyboard input  
- Saves keystrokes to `logs.txt`  
- Maps special keys to readable labels:
  - `Enter` → newline (`\n`)
  - `Tab` → tab (`\t`)
  - `Space` → `[SPACEBAR]`
  - `Backspace` → `[BACKSPACE]`
- Stops when the **Escape (ESC)** key is pressed

---

## 🧠 How It Works

1. A keyboard listener is started using `pynput.keyboard.Listener`.
2. Every key press is captured and converted to a string.
3. A dictionary is used to replace certain special keys with readable labels.
4. The result is written to `logs.txt`.
5. Pressing `ESC` will stop the keylogger and exit the script.

---

## 🚀 Usage

### 📦 Requirements

- Python 3.6+
- `pynput` module

Install `pynput` with:

```bash
pip install pynput
````

---

### ▶️ Run the Script

```bash
python keylogger.py
```

* The script will start logging keystrokes immediately.
* Output is saved to `logs.txt` in the same directory.
* To stop logging, press the **ESC** key.

---

## 📄 Sample Output (`logs.txt`)

```
't''e''s''t''i''n''g'[SPACEBAR]'k''e''y''l''o''g''g''e''r''s'[SPACEBAR]'i''n'[SPACEBAR]'p''y''t''h''o''n''.'\n
'd''a''t''a'[SPACEBAR]'l''o''g''g''e''d''!'[BACKSPACE][BACKSPACE][SPACEBAR]':)'\n
Key.ctrl's'Key.ctrl'v'
```

> Output may vary depending on user input.
> Special keys like `Space`, `Backspace`, or `Ctrl` combinations are shown as labeled tokens for readability.

---

## 📁 File Structure

```
Basic-Version/
├── README.md          # This file
└── keylogger.py       # Basic keylogger script
```

---

## ⚠️ Legal & Ethical Notice

This script is intended **only for educational and ethical use**.
Do **not** use it on any device you do not own or have explicit permission to monitor. Unauthorized use is illegal and unethical.

> The author assumes **no responsibility** for misuse.

```