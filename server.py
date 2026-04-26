# server.py
import socket

server = socket.socket()
server.bind(("0.0.0.0", 5000))   # Listen on port 5000
server.listen(1)

print("Server is waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

message = "Welcome to the Server!"
conn.send(message.encode())

conn.close()
server.close()