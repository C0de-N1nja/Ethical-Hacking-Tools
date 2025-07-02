# 🌐 ARP Network Scanner — Ethical Hacking Tool

A Python-based ARP scanner that identifies active devices on the local network using Scapy.  
It extracts their IP and MAC addresses and saves the data in a text file.

> ⚠️ This tool is intended for **educational use only** in authorized testing environments.

---

## ✅ Features

- 🔍 Scans LAN using ARP packets
- 🧾 Lists live hosts with IP and MAC addresses
- 📁 Saves output to `addresses.txt`
- 🛠 Accepts custom interface and optional IP range
- 💻 Simple command-line interface

---

## ⚙️ Requirements

- 🐍 Python 3.6+
- 🖥️ Linux system (tested on Kali Linux)
- 📦 [Scapy](https://scapy.readthedocs.io/en/latest/)

> Install Scapy:
```bash
pip install scapy
````

---

## 🚀 Usage

### 🔎 Basic Scan (Default Gateway Range)

```bash
sudo python3 arp_network_scanner.py --interface eth0
```

### 🎯 Custom IP Range

```bash
sudo python3 arp_network_scanner.py --interface eth0 --range 192.168.100.1
```

> Replace `eth0` with your interface (e.g., `wlan0`, `enp0s3`)
> `--range` is optional; if omitted, it auto-detects subnet

---

## 📁 Output

Results are saved to:

```text
addresses.txt
```

Sample output:

```
IP: 192.168.100.4   MAC: aa:bb:cc:11:22:33
IP: 192.168.100.5   MAC: dd:ee:ff:44:55:66
```

---

## 🧠 Notes

* 🔐 Requires root (`sudo`) privileges for raw socket access
* 🌐 Only works on Layer 2 local networks
* 🧱 Firewalls or antivirus may block ARP packets

---

## 🔗 Navigation

⬅️ [Back to All Tools](../../README.md)

---

## 👨‍💻 Author

**Muhammad Rehan Rashid**
🧠 GitHub Alias: [`C0de-N1nja`](https://github.com/C0de-N1nja)