#!/usr/bin/env python3

# Network Programming in Python: The Basics
# Isn't working because page use https insted of http

import socket
from urllib.parse import quote_plus

request_text = '''\
GET /search?q={}&format=json HTTP/1.1\r\n\
Host: nominatim.openstreetmap.org:80\r\n\
User-Agent: search4.py (Network Programming in Python: The Basics)\r\n\
Connection: close\r\n\

\r\n\
'''

def geocode(address):
	sock = socket.socket()
	sock.connect(('nominatim.openstreetmap.org', 80))
	request = request_text.format(quote_plus(address))
	sock.sendall(request.encode('ascii'))
	raw_reply = b''
	while True:
		more = sock.recv(4096)
		if not more:
			break

		raw_reply += more
	print(raw_reply.decode('utf-8'))


if __name__ == '__main__':
	geocode('taj mahal')
