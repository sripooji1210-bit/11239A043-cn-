import socket

def echo_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind and listen
    s.bind(('127.0.0.1', 65432))
    s.listen(1)
    print("Server is running and waiting for connection...")

    conn, addr = s.accept()
    print("Connected to:", addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break

        message = data.decode()
        print("Client says:", message)

        conn.sendall(data)  # echo back

    conn.close()
    s.close()

if __name__ == "__main__":
    echo_server()