# 🎯 Advanced Python Keylogger — Ethical Hacking Utility

This **Advanced Keylogger** is a stealthy, cross-platform surveillance utility built entirely in Python.  
It is designed for **ethical hacking**, **red teaming**, and **defensive security simulation** within authorized environments.

Unlike the basic version, this tool records every keystroke with full context — including modifier combos, clipboard events, active window titles, idle states, and more.

> ⚠️ For educational use only. Unauthorized use of keyloggers is illegal and unethical.

---

## 📁 Folder Structure

```

Advanced-Version/
├── README.md               # Tool documentation (this file)
└── advanced_keylogger.py   # Full-featured Python keylogger script

```

---

## 🚀 Why This Version?

The Basic Keylogger logs raw keypresses.  
This version takes it further — offering realistic simulation of stealth malware behavior for training, research, and red team scenarios.

---

## 🆚 Basic vs Advanced — Feature Comparison

| Feature                     | Basic Version   | Advanced Version                               |
|----------------------------|-----------------|------------------------------------------------|
| Keystroke Logging          | ✅ Yes          | ✅ Yes (w/ modifier combos)                    |
| Special Key Mapping        | ⚠️ Partial      | ✅ Full (F-keys, arrows, media, etc.)          |
| Modifier Detection         | ❌ No           | ✅ CTRL + ALT + SHIFT detection                |
| Active Window Tracking     | ❌ No           | ✅ Window title + process name                 |
| Idle/Resume Detection      | ❌ No           | ✅ Detects and logs user inactivity            |
| Timestamped Session Log    | ❌ No           | ✅ Timestamp + user/machine details            |
| Clipboard Monitoring       | ❌ No           | ✅ Clipboard capture on change                 |
| UTF-8 Logging              | ❌ No           | ✅ Multilingual and symbol-safe                |
| Cross-Platform Support     | ✅ Yes          | ✅ Yes (Windows + Linux)                       |

---

## 💡 Key Features Explained

### ⌨️ Keystroke Logging with Modifier Awareness

- Logs every key with readable formatting  
- Combines modifier keys like:
```

[CTRL + S], [SHIFT + ENTER], [ALT + TAB], [CTRL + SHIFT + ESC]

```
- Supports: F-keys, navigation keys, media controls, numpad

---

### 🖥️ Active Window + Process Tracking

- Detects foreground window every 200ms  
- Logs:
- Window title
- Process name (e.g., `code.exe`, `chrome.exe`)  
- Works on:
- Windows (via `win32gui`, `psutil`)
- Linux (via `xdotool`)

---

### 💤 Idle Time Detection

- Detects when the user is idle for 60+ seconds  
- Logs:
- `[User is Idle since: ...]`  
- `[User resumed at: ...]`  
- Useful for analyzing session pauses or break-ins

---

### 📋 Clipboard Monitoring

- Checks clipboard every 5 seconds  
- Logs timestamp + content  
- Skips duplicates to reduce noise

---

### 🧵 Threaded Architecture

- Main thread handles keylogging  
- Daemon threads handle:
- Idle tracking  
- Clipboard monitoring  
- Active window updates  
- Non-blocking and efficient

---

### 🧠 Smart Session Logging

- Log file starts with:
- Timestamp
- Hostname
- Logged-in user  
- Logs are named like:

```

logs 01-07-2025_03-20-55 AM.txt

````

---

### 🧩 Cross-Platform Compatible

- Automatically detects OS  
- Uses dynamic imports for platform-specific modules  
- Logs using UTF-8 for multilingual support

---

## ⚙️ Setup & Requirements

### 📦 Base Dependencies (All Platforms)

```bash
pip install pynput pyperclip
````

### 🪟 For Windows:

```bash
pip install pywin32 psutil
```

### 🐧 For Linux:

```bash
sudo apt install xdotool
```

---

## ▶️ Running the Keylogger

```bash
cd Advanced-Version/
python3 advanced_keylogger.py
```

* Starts logging immediately
* Press `ESC` to stop safely

---

## 📄 Sample Log Output

```
[Session started at: 01-07-2025_03-20-55 AM on Machine: beast by User: beast] 

Active Window: advanced_keylogger.py - Visual Studio Code (code.exe)

[CTRL + S][CTRL + V]This is a [BACKSPACE]demo[ENTER]

[Clipboard captured at: 01-07-2025_03:21:20 AM]
[Clipboard logged data:]
password123

[User is Idle since: 01-07-2025_03:24:00 AM]
[User resumed at: 01-07-2025_03:25:08 AM]

Active Window: GitHub - Chrome (chrome.exe)
```

---

## 🔐 Legal & Ethical Disclaimer

This tool is intended for **educational use and authorized testing** only.
Do **not** run this on devices or networks you do not own or have explicit written permission to test.

> The author assumes **no responsibility** for misuse, illegal deployment, or damage caused.

---

## 🔗 Navigation

* ⬅️ [Back to Keylogger Overview](../README.md)
* ⬅️ [Back to All Tools](../../../README.md)
* 🔹 [Go to Basic Version](../Basic-Version/README.md)

---

## 👨‍💻 Author

**Muhammad Rehan Rashid**
🧠 GitHub Alias: [`C0de-N1nja`](https://github.com/C0de-N1nja)