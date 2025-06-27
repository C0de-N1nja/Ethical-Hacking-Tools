import argparse
import os
import re
import subprocess
import time

def interface_down():
    # Down the interface to make the changings
    print("The interface is going to down!")
    time.sleep(1)
    subprocess.run(["ifconfig", interface, "down"])
    print("The interface is now down!")

def interface_up():
    # Up the interface after changings
    subprocess.run(["ifconfig", interface, "up"])
    time.sleep(1)
    print("The interface is now up!")

def show_current_mac():
    # Showing the currect MAC Address
    print("This is the current MAC Address of the system:")
    # current_mac = subprocess.check_output(f"ifconfig | grep {interface}", "| awk '{print $2}'", shell=True, text=True)
    current_mac = subprocess.check_output(f"ifconfig {interface} | grep ether | awk '{{print $2}}'", shell=True, text=True)
    print(current_mac)
    time.sleep(1)
    return current_mac

# Regex of MAC Address
mac_regex = "^(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})$"

# Use Argparse to make this script a command line utility
parser = argparse.ArgumentParser(description="Change the MAC address of a network interface.")
group = parser.add_mutually_exclusive_group(required=True)

parser.add_argument("-i", "--interface", help="Enter the interface name!", required=True)
group.add_argument("-m", "--mac", help="Enter the valid MAC address!")
group.add_argument("-o", "--old", action="store_true", help="Revert the Changings!")

args = parser.parse_args()
new_mac = args.mac
interface = args.interface

# Matching the given MAC with regex
if(new_mac):
    if(not re.match(mac_regex, new_mac)):
        print("Invalid MAC Address!")
        print("Example of a valid MAC address: 02:11:22:33:44:55")
        exit(1)

# Reverting Case
if(args.old):
    
    file1 = "original_mac.txt"
    if(not os.path.exists(file1)):
        print("The original mac file doesn't exist!")
        exit(1)
    
    current_mac = show_current_mac()        
    
    interface_down()
    with open(file1, 'r') as file:
        file_mac = file.read()
    
    # Storing the current MAC in file
    with open(file1, 'w') as file:
        file.write(current_mac)
        
    subprocess.run(["ifconfig", interface, "hw", "ether", file_mac])
    print("MAC Address reverted to ", file_mac)
    interface_up()
    exit(0)

current_mac = show_current_mac()

# Storing the current MAC in file
with open("original_mac.txt", 'w') as file:
    file.write(current_mac)

# Changing the MAC Address
time.sleep(1)
interface_down()
print("Changing MAC Address.....")
time.sleep(1)
subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
print("MAC Address is changed!")
interface_up()

# Showing the new MAC Address
print("Now showing you the changed MAC Address!")
subprocess.run([f"ifconfig {interface} | grep ether | awk '{{print $2}}'"], shell=True,)
