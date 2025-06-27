# ARP Network Scanner

A simple Python-based ARP network scanner that identifies active devices on a local network using Scapy. It extracts their IP and MAC addresses and stores the information in a text file.

## 🚀 Features

- Scans the local network via ARP requests.
- Lists live hosts with IP and MAC addresses.
- Saves results in `addressses.txt`.
- Accepts custom network interface and IP range.
- Command-line interface for flexible usage.

---

## 🧰 Requirements

- Python 3.6+
- Linux-based system (tested on Kali Linux)
- [Scapy](https://scapy.readthedocs.io/en/latest/) library

Install Scapy using pip:
```bash
pip install scapy
```

---

## ⚙️ Usage

```bash
sudo python3 arp_network_scanner.py --interface eth0
```

### Optional: Add IP Range

```bash
sudo python3 arp_network_scanner.py --interface eth0 --range 192.168.100.1
```

- `--interface` or `-i`: Network interface to scan (e.g., `eth0`, `wlan0`)
- `--range` or `-r`: (Optional) IP range to validate against the system default gateway

---

## 📁 Output

Results are saved in `addressses.txt` in the following format:

```
IP: 192.168.100.4   MAC: aa:bb:cc:11:22:33
IP: 192.168.100.5   MAC: dd:ee:ff:44:55:66
...
```

---

## 🛡️ Notes

- You must run the script with `sudo` or root privileges for packet crafting.
- Only works on local networks (Layer 2).
- Ensure your firewall/antivirus doesn't block ARP packets.

---
