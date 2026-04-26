import socket

# Create socket
server = socket.socket()

# Bind to localhost and port
server.bind(('localhost', 12345))

# Listen for connections
server.listen(1)
print("Server is waiting...")

# Accept connection
conn, addr = server.accept()
print("Connected to", addr)

while True:
    data = conn.recv(1024).decode()
    
    if not data:
        break
    
    print("Client:", data)
    
    # Send back same message
    conn.send(data.encode())

conn.close()
server.close()