# 🎯 Advanced Python Keylogger

This **Advanced Keylogger** is a stealthy, cross-platform surveillance utility built in Python. It is crafted for **ethical hacking**, **red teaming**, and **defensive security simulation** in authorized environments. Unlike the basic version, this tool records every keystroke with **intelligent context**—capturing modifier combinations, clipboard data, window focus, and even periods of user inactivity.

> ⚠️ This project is strictly for educational purposes. Unauthorized use of keyloggers is illegal and unethical.

---

## 📁 Directory Structure

```

Advanced-Version/
├── README.md               # You are here
└── advanced_keylogger.py   # Full-featured Python keylogger script

```

---

## 🚀 Why This Version?

While the basic keylogger simply logs raw keypresses, this version takes it to a **professional-grade** level—offering insights into real-world attack simulation with advanced logging behaviors.

---

## 🆚 Basic vs Advanced — Feature Comparison

| Capability                    | Basic Version   | Advanced Version                               |
|------------------------------|-----------------|------------------------------------------------|
| Keystroke Logging            | ✅ Yes          | ✅ Yes (w/ modifier combos)                    |
| Special Key Mapping          | ⚠️ Partial      | ✅ Full (Arrows, F-Keys, Media, etc.)          |
| Modifier Detection           | ❌ No           | ✅ CTRL + ALT + SHIFT combos                   |
| Active Window Tracking       | ❌ No           | ✅ Logs title + process name cross-platform    |
| Idle/Resume Logging          | ❌ No           | ✅ Logs idle time and return to activity       |
| Timestamped Session Logging  | ❌ No           | ✅ Begins with full timestamp + user info      |
| Clipboard Monitoring         | ❌ No           | ✅ Monitors and logs copied content            |
| UTF-8 Output Handling        | ❌ No           | ✅ Supports multilingual & special characters  |
| Cross-Platform Compatibility | ✅ Yes          | ✅ Yes (Windows + Linux)                       |

---

## 💡 Key Features in Detail

### ⌨️ Keystroke Logging with Modifier Intelligence

- Captures **every keypress** including letters, numbers, symbols, and special keys (arrows, function keys, etc.).
- **Combines modifier keys dynamically** like:

```

[CTRL + C], [SHIFT + ENTER], [ALT + TAB], [CTRL + SHIFT + ESC]

```

- Translates raw keycodes into human-readable labels (e.g., `[BACKSPACE]`, `[F12]`, `[VOL+]`)
- Handles numpad keys, special characters, and invisible key combinations.

> ✅ Gives a complete picture of user behavior, including shortcut usage and system navigation.

---

### 🖥️ Active Window + Process Monitoring (Cross-Platform)

- Checks the **foreground window title** every 200ms.
- Logs:
- Full window title
- Process name (e.g., `chrome.exe`, `code.exe`)
- Supports:
- Windows (via `win32gui`, `psutil`)
- Linux (via `xdotool` fallback)

> 🔍 Correlates user input with application context — like comparing typing in Chrome vs VS Code.

---

### 💤 Idle Time Detection & Resume Logging

- Detects when the system goes **idle for over 60 seconds**.
- Logs:
- `[User is Idle since: ...]`
- `[User resumed at: ...]`
- Uses a daemon thread to track inactivity in the background.

> 🧠 Helps analysts understand behavioral pauses, session gaps, or suspicious downtimes.

---

### 📋 Clipboard Capture on Change

- Monitors clipboard content **every 5 seconds**.
- Logs:
- Timestamp of each copy event
- Clipboard content
- Ignores duplicate entries to reduce noise.

> 🔐 Useful for detecting sensitive content (like copied passwords or credentials) without relying on typed keys.

---

### 🕵️ Threaded Stealth Design

- **Multi-threaded architecture**:
- Keystroke capture on main thread
- Idle monitor, clipboard logger, and window tracker as daemon threads
- All tasks are non-blocking and efficient.

> ⚙️ Mimics stealth malware behavior — lightweight, persistent, and silent.

---

### 🧠 Session Intelligence

- Begins each log file with:
- Timestamp
- Machine name (hostname)
- Current logged-in user
- Tracks first activity timestamp separately.
- Log files named by timestamp:

```

logs 01-07-2025_03-20-55 AM.txt

````

> 📜 Provides structured forensic insight into user activity from start to end.

---

### 🧩 OS-Aware Compatibility

- Automatically detects and adapts to Windows or Linux.
- Uses dynamic imports and fallbacks for platform-specific modules.
- Logs in **UTF-8** for multilingual and symbol-safe output.

> 🌍 Cross-platform, localization-aware, and fault-tolerant.

---

## ⚙️ Requirements & Setup

### 🐍 Python Dependencies

Install the base modules:

```bash
pip install pynput pyperclip
````

#### ▶️ Windows Only:

```bash
pip install pywin32 psutil
```

#### ▶️ Linux Only:

```bash
sudo apt install xdotool
```

---

## ▶️ Running the Keylogger

1. Open terminal in the `Advanced-Version/` directory.
2. Run:

```bash
python3 advanced_keylogger.py
```

3. All logs will be saved with timestamps like:

```
logs 01-07-2025_03-20-55 AM.txt
```

> ✅ Press `ESC` to stop logging and exit safely.

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

## 🔐 Legal & Ethical Use

This tool is for **educational and authorized security testing** only.

By using this software, you agree to:

* Only test systems you **own** or are **authorized to audit**
* Never deploy it without **explicit consent**
* Take **full responsibility** for all actions

> ❌ The author assumes **no liability** for misuse or unethical deployment.

---

## 🌐 Part of a Larger Toolkit

This advanced keylogger is part of the [`C0de-N1nja-Ethical-Hacking-Tools`](https://github.com/C0de-N1nja) collection — a practical, Python-based toolkit for red teamers, students, and security enthusiasts.

> **Think like an attacker. Learn like a hacker. Defend like a pro. 🥷**

