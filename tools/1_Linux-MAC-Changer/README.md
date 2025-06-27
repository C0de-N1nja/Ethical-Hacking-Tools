# 🛡️ MAC Changer — Ethical Hacking Tool

A simple Python script to **change** or **revert** the MAC address of a network interface.  
Useful for learning **network spoofing** and **privacy techniques**.
🖥️ Linux-only tool

---

## ✅ Features

- Change MAC address via CLI  
- Revert to original MAC  
- Automatically saves original MAC  

---

## ⚙️ Requirements

- Python 3  
- `net-tools` (for `ifconfig`)  
- Must be run with `sudo`  

---

## 🚀 Usage

### 🔧 Change MAC Address
```bash
sudo python3 tools/mac_changer.py -i wlp3s0 -m 02:11:22:33:44:55
```

### ♻️ Revert to Original MAC
```bash
sudo python3 tools/mac_changer.py -i wlp3s0 -o
```

---

## 📁 Output

- Saves original MAC in `original_mac.txt`

---

## ⚠️ Disclaimer

> This tool is for **educational purposes only**.  
> Do **not** use it on unauthorized networks.

