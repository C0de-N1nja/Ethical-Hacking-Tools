🛡️ MAC Changer — Ethical Hacking Tool
A simple Python script to change or revert the MAC address of a network interface. Useful for learning network spoofing and privacy techniques.

✅ Features
Change MAC address via CLI

Revert to original MAC

Saves original MAC automatically

⚙️ Requirements
Python 3

net-tools (ifconfig)

Run as sudo

🚀 Usage
Change MAC:

bash
Copy
Edit
sudo python3 tools/mac_changer.py -i wlp3s0 -m 02:11:22:33:44:55
Revert MAC:

bash
Copy
Edit
sudo python3 tools/mac_changer.py -i wlp3s0 -o
📁 Output
Stores original MAC in original_mac.txt

⚠️ Disclaimer
For educational use only. Do not use on unauthorized networks.
