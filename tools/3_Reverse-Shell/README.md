# 🐚 Reverse Shell in Python — Basic & Advanced Versions

This module demonstrates how to build a **reverse shell** in Python — starting from a foundational one-time connection and scaling up to a robust, reconnecting, feature-rich remote access tool.

It’s split into two versions:
- 🔹 A **Basic** reverse shell for foundational understanding
- 🔸 An **Advanced** reverse shell for real-world simulation, red teaming, or blue team detection practice

> ⚠️ Use only in authorized testing environments. This project is strictly for educational and ethical hacking practice.

---

## 📁 Folder Structure

```

Reverse-Shell/
├── README.md                  # General project overview (this file)
├── Basic-Version/
│   ├── README.md              # Detailed explanation of the basic version
│   ├── hacker.py              # Basic reverse shell listener
│   └── victim.py              # Basic reverse shell payload
└── Advanced-Version/
    ├── README.md              # Detailed explanation of the advanced version
    ├── advanced_hacker.py     # Robust listener with upload/download & error handling
    └── advanced_victim.py     # Payload with reconnection, download/upload, and full shell support

````

---

## 🧠 What is a Reverse Shell?

A **reverse shell** is a remote access technique where a victim’s machine initiates a connection to the attacker's machine.  
This allows the attacker to execute system-level commands on the victim — especially useful when the victim is behind a **firewall or NAT**.

---

## 🧪 Version Comparison

### ✅ Basic Version
- One-time socket connection
- Simple command execution
- Basic send/receive loop
- Minimal error handling

📄 [View Basic Version README](./Basic-Version/README.md)

---

### 🚀 Advanced Version
- Persistent reconnection (listener restart-resistant)
- File download/upload with progress
- Cross-platform encoding (Windows/Linux safe)
- Screenshot capture from victim
- Robust error handling and graceful exit

📄 [View Advanced Version README](./Advanced-Version/README.md)

---

## 🛠️ Requirements

- 🐍 Python 3.6+
- 🖥️ Works on Linux & Windows
- Some advanced features require:
  - `mss` for screenshots
  - `os`, `socket`, `threading`, etc. (standard libs)

Install any missing dependencies with:

```bash
pip install mss
````

---

## 🧠 Use Cases

Use this project to:

* 🧪 Understand socket programming
* 🛠️ Simulate attacker behavior in a lab
* 🔁 Build adaptable reverse shell tools
* 🧩 Learn command execution, reconnection, and file transfer techniques

---

## 🔐 Ethical Disclaimer

> This tool is for **educational and ethical hacking purposes only**.
> Unauthorized use on systems or networks **you do not own or have explicit permission to test** is strictly prohibited.

See [LICENSE](../../LICENSE) for full legal terms.

---

## 🔗 Navigation

- ⬅️ [Back to All Tools](../../README.md)  
- 🔹 [Basic Reverse Shell](./Basic-Version/README.md)  
- 🔸 [Advanced Reverse Shell](./Advanced-Version/README.md)

---

## 👨‍💻 Author

**Muhammad Rehan Rashid**
🧠 GitHub Alias: [`C0de-N1nja`](https://github.com/C0de-N1nja)