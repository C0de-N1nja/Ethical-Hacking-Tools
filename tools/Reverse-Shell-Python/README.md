# 🐍 Reverse Shell in Python

This project demonstrates how a Python-based reverse shell can be built and enhanced in a modular and stealthy way. It is structured to show both a **Basic** version and an **Advanced** version of a reverse shell, offering a clear path from foundational learning to more robust, feature-rich tools — useful for ethical hacking, red teaming, or defensive simulation in cybersecurity.

---

## 📁 Directory Structure

```

Reverse-Shell-Python/
├── README.md                  # General project overview (this file)
├── Basic-Version/
│   ├── README.md              # Detailed explanation of the basic version
│   ├── hacker.py              # Basic reverse shell listener
│   └── victim.py              # Basic reverse shell payload
└── Advanced-Version/
    ├── README.md              # Detailed explanation of the advanced version
    ├── advanced\_hacker.py     # Robust listener with upload/download & error handling
    └── advanced\_victim.py     # Payload with reconnection, download/upload, and full shell support

```

---

## 📜 What is a Reverse Shell?

A reverse shell is a type of remote shell where the victim machine initiates a connection to the attacker’s machine, allowing the attacker to execute commands on the victim's system.

> This is especially useful in scenarios where the victim is behind a firewall or NAT, and direct connections are not possible.

---

## 🧪 Versions Explained

### ✅ Basic Version
- One-time connection
- Executes shell commands
- Simple send/receive logic
- Limited error handling

➡️ [View Basic Version Details](./Basic/README.md)

---

### 🚀 Advanced Version
- Automatic reconnection if the listener is restarted
- Command execution with encoding fallback (Windows/Linux compatible)
- File download from victim to attacker
- File upload from attacker to victim
- Graceful disconnection and error handling

➡️ [View Advanced Version Details](./Advanced/README.md)

---

## ⚠️ Disclaimer

This tool is for educational and ethical hacking purposes only. You must obtain proper authorization before deploying this in any real-world environment. The author assumes no liability for misuse.

---

## 🧠 Recommended Use Case

Use this project to:
- Learn reverse shell mechanics in Python
- Practice handling sockets, encoding, and binary data
- Simulate red teaming scenarios in controlled environments

---

## 🛠️ Requirements

- Python 3.6+
- Works on both Windows and Linux

---

