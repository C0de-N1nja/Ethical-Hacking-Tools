# 🧠 C0de-N1nja Ethical Hacking Toolkit

A curated collection of real-world, Python-based **ethical hacking tools** for learning, red teaming, simulation, and penetration testing — developed and maintained by **Muhammad Rehan Rashid (aka C0de-N1nja)**.

This repository is intended for **educational use**, helping cybersecurity students, professionals, and researchers understand how offensive tools work under the hood — **ethically and legally**.

> ⚠️ All tools are for **authorized testing and educational purposes only**. Unauthorized use is illegal and punishable under cybercrime laws.

---

## 🏷️ Badges

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
![Ethical Use Only](https://img.shields.io/badge/Ethical--Use-Authorized%20Only-red)  
[![Made by](https://img.shields.io/badge/Made%20by-C0de--N1nja-purple)](https://github.com/C0de-N1nja)

---

## 🎯 Purpose

The goal of this repository is to:

- Provide **practical tools** for ethical hackers and red teamers
- Offer a **learning ground** for cybersecurity students and professionals
- Demonstrate **real-world offensive techniques** in a controlled, responsible, and legal way

This repo helps you explore areas like:

- 🔁 Remote access (reverse shells)  
- 🔍 Reconnaissance and scanning  
- 🎯 Credential harvesting  
- 📂 File system interaction  
- 🧱 Persistence and command execution  
- 🌐 Network manipulation

---

## 💼 Intended Audience

- Cybersecurity students  
- Ethical hackers and pentesters  
- CTF participants  
- Researchers studying offensive security

> ⚠️ This repository assumes you know the basics of networking, operating systems, Python scripting, and ethical guidelines.

---

## 🛠️ Tools Included

| Tool                           | Description                                                     | Platform        |
|--------------------------------|-----------------------------------------------------------------|-----------------|
| 🔧 [MAC Changer](tools/1_Linux-MAC-Changer/)              | Spoof or reset your MAC address via CLI                       | Linux           |
| 🌐 [ARP Network Scanner](tools/2_ARP-Network-Scanner/)     | Discover devices on LAN using ARP & Scapy                     | Linux           |
| 🐚 [Reverse Shell (Basic)](tools/3_Reverse-Shell/Basic-Version/) | Minimal Python reverse shell (client-server)                 | Linux + Windows |
| 🧰 [Reverse Shell (Advanced)](tools/3_Reverse-Shell/Advanced-Version/) | Robust version with upload, screenshot, reconnection, and more | Cross-platform  |
| ⌨️ [Keylogger (Basic)](tools/4_Keylogger/Basic-Version/)   | Logs keypresses to a file                                     | Cross-platform  |
| 🧠 [Keylogger (Advanced)](tools/4_Keylogger/Advanced-Version/) | Clipboard capture, modifier detection, active window logging, idle tracking | Cross-platform |

---

## 🧭 Quick Navigation

- 🔗 [Advanced Reverse Shell](tools/3_Reverse-Shell/Advanced-Version/README.md)
- 🔗 [Advanced Keylogger](tools/4_Keylogger/Advanced-Version/README.md)

---

## ✨ Features

- ✅ Python-only, cross-platform tools (Linux + Windows)
- ✅ Clean modular structure with tool-specific README files
- ✅ Modifier-aware keystroke logging with clipboard capture
- ✅ Screenshot capture and file transfers in reverse shell
- ✅ Persistent reconnection logic for reliable sessions
- ✅ Active window & idle tracking in keylogger
- ✅ Legal disclaimers and ethical use notices in every tool
- ✅ Output samples and command-line usage examples included

---

## 🚀 How to Use

Each tool is self-contained in its own folder under `/tools/` and includes a dedicated `README.md` with:

- ✅ Tool overview  
- 🧠 Technical breakdown  
- ⚙️ Setup instructions  
- 🎯 Use cases  
- ⚠️ Limitations or caveats

Basic usage:

```bash
git clone https://github.com/C0de-N1nja/Ethical-Hacking-Tools.git
cd Ethical-Hacking-Tools/tools/<tool-folder>/
python3 script.py
````

---

## 📦 Setup Requirements

Install shared dependencies for all tools:

```bash
pip install pynput pyperclip scapy mss psutil pywin32
```

> Some tools may require additional OS packages like `xdotool` (Linux) or `pywin32` (Windows).

---

## 🔐 Responsible Usage

By using this repository, you agree that:

* You are solely responsible for your actions
* You will not use these tools for unauthorized access or disruption
* You will only test in environments you **own or have written permission to access**
* You understand these tools are for **ethical, educational purposes only**

> See [LICENSE](LICENSE) for full legal terms.

---

## 👨‍💻 Author

**Muhammad Rehan Rashid**
🧠 GitHub Alias: [`C0de-N1nja`](https://github.com/C0de-N1nja)

---

## 🧩 Part of a Bigger Learning Journey

This repository is part of my 2025 self-guided journey in **cybersecurity, red teaming, and ethical hacking**. Each tool represents both technical understanding and a hands-on approach to simulating real-world attacker behavior.

> **Think like an attacker. Learn like a hacker. Defend like a pro. 🥷**