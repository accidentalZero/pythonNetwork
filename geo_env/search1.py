#!/usr/bin/env python3

# Network Programming in Python: The Basics
# Isn't working because google require token

from pygeocoder import Geocoder


if __name__ == '__main__':
	address = 'taj mahal'
	print(Geocoder.geocode(address)[0].coordinates)

