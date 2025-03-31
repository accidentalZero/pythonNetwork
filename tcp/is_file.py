import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(hasattr(sock, 'read'))

f = sock.makefile()
print(hasattr(f, 'read'))
