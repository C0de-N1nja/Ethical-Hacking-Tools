# 🐍 Python Reverse Shell — Basic Version

This project demonstrates a **basic reverse shell** using Python's built-in `socket` module.  
It enables remote command execution on a victim machine once a connection is established with an attacker's listener.

> ⚠️ For **educational and ethical hacking** purposes only. Do **not** use this on unauthorized systems or networks.

---

## 📁 Folder Contents

```

Basic-Version/
├── hacker.py         # Attacker script (command and control)
├── victim.py         # Victim script (connects back to attacker)
└── README.md         # This file

````

---

## 🧠 How It Works

- 🧷 `victim.py` continuously attempts to connect to the attacker's IP and port.
- 🖥️ `hacker.py` listens for incoming connections and provides a command prompt.
- Once connected:
  - Commands are sent from attacker to victim.
  - Output is returned and displayed.
  - Commands like `cd`, `mkdir`, `type`, and others are supported.

---

## ✨ Features

- 🔁 **Persistent connection**: Victim retries every 5 seconds if attacker is offline
- 📂 **Directory navigation**: Supports `cd`, `cd ..`, etc.
- ⚙️ **Silent command support**: Shows success messages even when command has no output
- 🔐 **Graceful exit**: `stop` command cleanly closes the session
- 🌐 **Cross-platform**: Works on Linux and Windows
- ❌ **No external libraries** needed (pure `socket` + built-ins)

---

## ⚙️ Setup Instructions

### 🔧 1. Configure IP and Port

In **both scripts**, set:

```python
hacker_ip = "192.168.100.17"  # Replace with your attacker's IP
hacker_port = 10000           # Port to listen/connect on
````

> Use `ipconfig` (Windows) or `ifconfig` / `ip a` (Linux) to find your IP

---

## 🚀 Usage

### 🖥️ On Attacker Machine (`hacker.py`)

```bash
python3 hacker.py
```

* Starts a TCP listener
* Waits for victim to connect
* Prompts for commands after connection

### 🧷 On Victim Machine (`victim.py`)

```bash
python3 victim.py
```

* Attempts to connect to attacker
* Executes received commands

> If the attacker isn’t available, victim retries every 5 seconds.

---

## 💡 Supported Commands

| Command           | Behavior                        |
| ----------------- | ------------------------------- |
| `cd`              | Show current working directory  |
| `cd <path>`       | Change working directory        |
| `mkdir <folder>`  | Create a folder (shows success) |
| `type <file>`     | Read a file (Windows)           |
| `ls`, `dir`       | List directory contents         |
| Any shell command | Execute and return output       |
| `stop`            | Gracefully disconnect           |

### 🧪 Example Interaction

```bash
Enter command to execute on victim: cd
Current directory: C:\Users\Target

Enter command to execute on victim: mkdir testfolder
mkdir testfolder executed successfully (no output)!

Enter command to execute on victim: type secrets.txt
password123!
```

---

## 📦 Output Handling

* Success messages shown even if command produces no output
* Errors (e.g., command not found) are returned to attacker

---

## 🔒 Limitations & Future Improvements

| Area          | Current Status           | Suggested Upgrade                   |
| ------------- | ------------------------ | ----------------------------------- |
| Encryption    | ❌ Unencrypted            | Add SSL/TLS or symmetric encryption |
| Multi-client  | ❌ Single connection only | Use threading for multiple victims  |
| File transfer | ❌ Not supported          | Add upload/download functionality   |
| Stealth       | ❌ Runs visibly           | Convert to daemon/background task   |

---

## 📜 Legal & Ethical Disclaimer

This project is provided for **educational use only**.
Running this on machines or networks you do not **own or have written permission to test** is illegal.

> The author is **not responsible** for any misuse or illegal activity involving this code.

---

## 🔗 Navigation

⬅️ [Back to Reverse Shell Overview](../README.md)
⬅️ [Back to All Tools](../../../README.md)

---

## 👨‍💻 Author

**Muhammad Rehan Rashid**
🧠 GitHub Alias: [`C0de-N1nja`](https://github.com/C0de-N1nja)