import socket
import threading
import time
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 15432  # The port used by the server

state = True
def reciever(s):
    global state
    while state:
        data = s.recv(1024).decode("utf-8")
        print("Server: " + data)
def test_ping_loop(s): # just to show what is possible
    global state
    while state:
        time.sleep(1)
        s.sendall(bytes("HeartBeat", "utf-8"))
        
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("starting threads")
    x = threading.Thread(target=reciever, args=(s,))
    x.start()
    y = threading.Thread(target=test_ping_loop, args=(s,))
    y.start()
    print("threads run")
    while state:
        """for test commands or other stuff lmao"""
        a = input()
        b = bytes(a, "utf-8")
        s.sendall(b)
        if a == "fin":
            state = False
    s.close()