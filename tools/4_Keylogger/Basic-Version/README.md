# 📄 Basic Python Keylogger — Educational Version

This script demonstrates a minimal **keylogger** built in Python using the `pynput` library.  
It captures all keystrokes from the keyboard and logs them to a local file (`logs.txt`).

Ideal for cybersecurity students and beginners, this script offers a clear, foundational understanding of how keylogging works — entirely for ethical learning and simulation.

---

## ✨ Features

- 🔹 Captures all keyboard input
- 🔹 Logs to `logs.txt` in real time
- 🔹 Maps special keys to readable labels:
  - `Enter` → `\n`
  - `Tab` → `\t`
  - `Space` → `[SPACEBAR]`
  - `Backspace` → `[BACKSPACE]`
- 🔹 Pressing `ESC` cleanly stops the logger

---

## 🧠 How It Works

1. Starts a keyboard listener using `pynput.keyboard.Listener`
2. Detects every key press and parses to string
3. Replaces special keys with labeled tokens
4. Writes each stroke to a log file
5. Stops on `ESC` key press

---

## 📦 Requirements

- 🐍 Python 3.6+
- 📦 [`pynput`](https://pypi.org/project/pynput/)

Install `pynput`:

```bash
pip install pynput
````

---

## 🚀 Usage

### ▶️ Run the Script

```bash
python3 keylogger.py
```

* Script begins logging immediately
* All keystrokes go to `logs.txt` (same directory)
* Press `ESC` to stop logging

---

## 📄 Sample Output (`logs.txt`)

```
't''e''s''t''i''n''g'[SPACEBAR]'k''e''y''l''o''g''g''e''r''s'[SPACEBAR]'i''n'[SPACEBAR]'p''y''t''h''o''n''.'\n
'd''a''t''a'[SPACEBAR]'l''o''g''g''e''d''!'[BACKSPACE][BACKSPACE][SPACEBAR]':)'\n
Key.ctrl's'Key.ctrl'v'
```

> Output may vary based on typing.
> Special keys are labeled for readability.

---

## 📁 Folder Structure

```
Basic-Version/
├── README.md          # Tool documentation (this file)
└── keylogger.py       # Basic keystroke logging script
```

---

## ⚠️ Legal & Ethical Disclaimer

This tool is intended strictly for **educational and authorized testing**.
Running this script on devices or systems you do **not own or have explicit permission to test** is **illegal** and may violate cybercrime laws.

> The author assumes **no responsibility** for any misuse or damage caused by this tool.

---

## 🔗 Navigation

* ⬅️ [Back to Keylogger Overview](../README.md)
* ⬅️ [Back to All Tools](../../../README.md)

---

## 👨‍💻 Author

**Muhammad Rehan Rashid**
🧠 GitHub Alias: [`C0de-N1nja`](https://github.com/C0de-N1nja)