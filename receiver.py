
import socket

host = '192.168.26.75'  #write the ip adress on which you are using camera that is server
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
    print("Connected to server")
    while True:
        msg = s.recv(1024).decode()
        if not msg:
            break
        print("Received:", msg)
except Exception as e:
    print(f"Client error: {e}")
finally:
    s.close()
