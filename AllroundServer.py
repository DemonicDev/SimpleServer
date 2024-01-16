HOST = "127.0.0.1" 
PORT = 15432
bound_clients = {}
g = 0
def Connection(conn):
    global bound_clients
    global g
    h = g
    bound_clients[h] = conn
    g += 1
    with conn:
        ##try to catch random disconnect by client ;)
        try:
            while True:
                data = conn.recv(1024).decode("utf-8")
                print("Received " + data)
                if(data == "fin"):
                    #conn.close()
                    break
                elif(data == "HeartBeat"):
                    conn.sendall(bytes("HeartBeat recieved" ,"utf-8"))
                    continue
                for i in bound_clients:
                    j = bound_clients[i]
                    if not j == conn:
                        j.sendall(bytes(data, "utf-8"))
        except ConnectionResetError as e:
            print(f"ConnectionResetError: {e}")            
        finally:
            del(bound_clients[h])
            conn.close()
                    

import socket
import threading

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        print("starting new thread for incomming connection request")
        x = threading.Thread(target=Connection, args=(conn,))
        x.start()
        print("thread started :>")