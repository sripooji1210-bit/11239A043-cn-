import socket

# Create socket
client = socket.socket()

# Connect to server
client.connect(('localhost', 12345))

while True:
    msg = input("Enter message: ")
    
    client.send(msg.encode())
    
    data = client.recv(1024).decode()
    print("Server:", data)
    
    if msg.lower() == "exit":
        break

client.close()