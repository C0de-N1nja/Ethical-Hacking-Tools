import argparse
import re
import subprocess
import time

# Regex of MAC Address
mac_regex = "^(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})$"

# Use Argparse to make this script a command line utility
parser = argparse.ArgumentParser(description="Change the MAC address of a network interface.")
parser.add_argument("-m", "--mac", help="Enter the valid MAC address!", required=True)
parser.add_argument("-i", "--interface", help="Enter the interface name!", required=True)

args = parser.parse_args()
new_mac = args.mac
interface = args.interface

# Matching the given MAC with regex
if(not re.match(mac_regex, new_mac)):
    print("Invalid MAC Address!")
    print("Example of a valid MAC address: 02:11:22:33:44:55")
    exit(1)

# Showing the currect MAC Address
print("This is the current MAC Address of the system:")
subprocess.run(["ifconfig | grep ether"], shell=True,)
time.sleep(1)

# Down the interface to make the changings
print("The interface is going to down!")
time.sleep(1)
subprocess.run(["ifconfig", interface, "down"])
print("The interface is now down!")

# Changing the MAC Address
time.sleep(1)
print("Changing MAC Address.....")
time.sleep(1)
subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
print("MAC Address is changed!")

# Up the interface after changings
subprocess.run(["ifconfig", interface, "up"])
time.sleep(1)
print("Now showing you the changed MAC Address!")

# Showing the new MAC Address
subprocess.run(["ifconfig | grep ether"], shell=True,)