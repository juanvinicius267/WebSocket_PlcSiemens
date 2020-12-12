import socket

HOST = '10.251.16.66'
PORT = 2000

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.connect((HOST,PORT))
        print(conn.recv(1024).decode('UTF-8', errors = 'ignore'))
        conn.close()
        conn2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        PORT2 = 2001
        conn2.connect((HOST,PORT2))
        conn2.sendall('Hello, world')
        conn2.close()



