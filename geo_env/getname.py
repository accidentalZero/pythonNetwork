#!/usr/bin/env python3

# Network Programming in Python: The Basics
import socket


if __name__ == '__main__':
	hostname = 'www.python.org'
	addr = socket.gethostbyname(hostname)
	print('The IP address of {} is {}'.format(hostname, addr))
