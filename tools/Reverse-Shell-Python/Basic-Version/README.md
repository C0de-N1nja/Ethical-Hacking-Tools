# 🐍 Python Reverse Shell

This project is a basic **reverse shell** built using Python's `socket` module. It enables remote command execution on a victim machine once a connection is established to an attacker's listener.

> ⚠️ This tool is strictly for **educational** and **ethical hacking** purposes on systems you own or have permission to test. Unauthorized use is illegal.

---

## 📁 Project Structure

```

Basic-Version/
├── hacker.py         # Attacker script (command and control)
├── victim.py         # Victim script (connects back to attacker)
├── README.md         # Project documentation

````

---

## 🧠 How It Works

- The attacker (`hacker.py`) listens for incoming connections.
- The victim (`victim.py`) tries to connect to the attacker repeatedly (every 5 seconds if offline).
- Once connected, the attacker can:
  - Send system commands to the victim.
  - Change directories.
  - Execute silent commands like `mkdir`.
  - Terminate the session gracefully.

---

## ✨ Features

- **Persistent Connection Attempts:** Victim continuously tries to connect if attacker is offline.
- **Directory Navigation:** Support for `cd` command with current directory display.
- **Silent Command Handling:** Commands that don’t produce output return success messages.
- **Command Execution:** Execute arbitrary shell commands remotely.
- **Graceful Termination:** `stop` command cleanly closes the connection.
- **Error Handling:** Errors and failed commands return meaningful output.
- **Cross-Platform Compatibility:** Works on Windows and Linux (commands may vary).

---

## ⚙️ Setup Instructions

### ✅ Step 1: Configure IP and Port

Both `hacker.py` and `victim.py` must have the same IP and port set in their code.

#### In both files:
```python
hacker_ip = "192.168.100.17"  # Replace with attacker's IP address
hacker_port = 10000           # Port to use
````

> 📌 Use your **local IP address** if testing on a local network. You can find it using:
>
> * On Windows: `ipconfig`
> * On Linux/macOS: `ip a` or `ifconfig`

---

## 🚀 Usage

### 🖥️ On Attacker Machine (`hacker.py`)

```bash
python3 hacker.py
```

* Starts a TCP listener.
* Waits for a victim to connect.
* Prompts you to enter commands after connection.

### 🧷 On Victim Machine (`victim.py`)

```bash
python3 victim.py
```

* Tries to connect to the attacker's IP and port.
* Executes any commands sent by the attacker.

> If the attacker is not online, it will retry every 5 seconds.

---

## 💡 Supported Commands and Behaviors

| Command            | Behavior                                          |
| ------------------ | ------------------------------------------------- |
| `cd`               | Shows current working directory on victim.        |
| `cd path`          | Changes working directory on victim.              |
| `mkdir foldername` | Creates a folder (no output unless error).        |
| `type filename`    | Displays contents of file (like `cat` on Linux).  |
| `dir` / `ls`       | Lists directory contents.                         |
| Any shell command  | Executes and returns output.                      |
| `stop`             | Gracefully ends the session from the hacker side. |

### Example Interaction

```bash
Enter command to execute on victim: cd
Current directory: C:\Users\Target

Enter command to execute on victim: mkdir testfolder
mkdir testfolder executed successfully (no output)!

Enter command to execute on victim: type secrets.txt
password123!
```

---

## 🧪 Output Handling

* If a command gives **no output**, a success message is shown anyway:

  ```
  mkdir test executed successfully (no output)!
  ```
* All errors are captured and sent back.

---

## 🔒 Limitations & Ideas for Improvement

| Area          | Current Status            | Suggestions                       |
| ------------- | ------------------------- | --------------------------------- |
| Encryption    | ❌ Plaintext communication | Use `ssl` or `cryptography` lib   |
| Multi-client  | ❌ Single client only      | Use threading or multiprocessing  |
| File transfer | ❌ Not implemented         | Add upload/download functionality |
| Stealth       | ❌ Not hidden              | Convert to background task        |

---

## 📜 Legal Disclaimer

This project is intended for **educational use only**. Running this code on machines you do not own or lack permission to test is **illegal** and punishable by law. The creator is **not responsible** for any misuse.

---
