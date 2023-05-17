import socket
import paramiko
import threading

class SSHServer(paramiko.ServerInterface):
    def check_auth_password(self, username: str, password: str) -> int:
        print(f"{username}:{password}")
        return paramiko.AUTH_FAILED

def handle_connection(client_sock):
    transport = paramiko.Transport(client_sock)
    # server_key = paramiko.RSAKey.generate(2048)
    server_key = paramiko.RSAKey.from_private_key_file('key')
    transport.add_server_key(server_key)
    ssh = SSHServer()
    transport.start_server(server=ssh)

def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('', 2222))
    server_sock.listen(233)

    while True:
        client_sock, client_addr = server_sock.accept()
        print(f"Connection from {client_addr[0]}:{client_addr[1]}")
        # client_sock.send(b"Hello!\n")
        # print(client_sock.recv(256).decode())
        t = threading.Thread(target=handle_connection, args=(client_sock,))
        t.start()


if __name__ == "__main__":
    main()

