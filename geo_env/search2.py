#!/usr/bin/env python3

# Network Programming in Python: The Basics

import requests

def geocode(address):
	base = 'https://nominatim.openstreetmap.org/search'
	parameters = {'q': address, 'format': 'json'}
	user_agent = 'Client-Server Networking: An Overview search2.py'
	headers = {'User-Agent': user_agent}
	response = requests.get(base, params=parameters, headers=headers)
	reply = response.json()
	print(reply[0]['lat'], reply[0]['lon'])
	#return reply


if __name__ == '__main__':
	geocode('taj mahal')
	#print(geocode('taj mahal'))
