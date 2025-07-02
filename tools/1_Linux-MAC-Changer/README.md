# 🔧 MAC Changer — Ethical Hacking Tool

A Python-based tool to **change** or **revert** the MAC address of a network interface on Linux.  
Useful for understanding **network spoofing**, **device anonymity**, and **basic privilege escalation concepts**.

> ⚠️ This tool is for **educational use only**. Do **not** use it on networks you don't own or control.

---

## ✅ Features

- 🔁 Change your MAC address via command line
- 💾 Automatically stores the original MAC
- ♻️ Revert back to the original MAC with a flag
- 📂 Stores original MAC in `original_mac.txt`

---

## ⚙️ Requirements

- 🐍 Python 3.x
- 🛠️ `net-tools` (`ifconfig`)
- 🔐 Must be run with `sudo`

---

## 🚀 Usage

### 🆕 Change MAC Address
```bash
sudo python3 mac_changer.py -i wlp3s0 -m 02:11:22:33:44:55
````

### 🔙 Revert to Original MAC

```bash
sudo python3 mac_changer.py -i wlp3s0 -o
```

> Replace `wlp3s0` with your actual network interface (e.g., `eth0`, `enp0s3`)

---

## 📁 Output

Creates a file named:

```
original_mac.txt
```

This file stores the original MAC address for easy restoration.

---

## 🧠 Ethical & Legal Use

This tool is intended strictly for **authorized testing and educational labs**.
Do not use this script on public or unauthorized networks.

---

## 🔗 Navigation

⬅️ [Back to All Tools](../../README.md)

---

## 👨‍💻 Author

**Muhammad Rehan Rashid**
🧠 GitHub Alias: [`C0de-N1nja`](https://github.com/C0de-N1nja)