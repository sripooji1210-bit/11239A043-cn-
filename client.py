# client.py
import socket

client = socket.socket()
client.connect(("127.0.0.1", 5000))   # Connect to server

message = client.recv(1024).decode()
print("Message from server:", message)

client.close()