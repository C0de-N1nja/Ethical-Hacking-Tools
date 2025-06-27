import argparse
import subprocess
from scapy.all import Ether, ARP, srp

parser = argparse.ArgumentParser(description="A Network Scanner.")
parser.add_argument("--interface", "-i", help="Enter the interface name!", required=True)
parser.add_argument("--range", "-r", help="Enter the Range of your Network!")

args = parser.parse_args()

interface = args.interface
ip_range = args.range

broadcast = "FF:FF:FF:FF:FF:FF"

ether_layer = Ether(dst = broadcast)

default_range = subprocess.check_output("ip route | grep default | awk '{print$3}'", shell=True)
default_range = default_range.decode().strip()

if(ip_range):
    if(ip_range != default_range):
       print("The given IP range is not correct!") 
       exit(1)
    
    ip_range = default_range + "/24"
    arp_layer = ARP(pdst = ip_range)

if(not ip_range):
    default = default_range + "/24"
    arp_layer = ARP(pdst = default)

packet = ether_layer/arp_layer

ans ,unans = srp(packet, interface, timeout=2)

filename = "addressses.txt"
if(filename):
    subprocess.run(["rm", filename])

for send, recv in ans:
    ip = recv[ARP].psrc
    mac = recv[Ether].src
    
    with open(filename, 'a') as file:
        file.write("IP: " + ip + "   " + "MAC: " + mac + "\n")

    print(f"IP: {ip}, MAC: {mac}")
    
