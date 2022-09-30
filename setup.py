#! /usr/bin/python3

import os

try:
	import socket
except:
	os.system("pip install socket")
try:
	import pyfiglet
except:
	os.system("pip install pyfiglet")
try:
	import termcolor
except:
	os.system("pip install termcolor")
try:
	import base64
except:
	os.system("pip install base64")


def make():
	try:
		os.system("sudo chmod +x sc4nit.py")
	except:
		print ("[!!]Unable to make executable")
	try:
		os.system("cp sc4nit.py /usr/local/bin")
		os.system("cp -r package /usr/local/bin")
	except:
		print ("[!!]Unexpected error")

if (os.getuid == 0):
	make()
else:
	print ("[!!]Root privileges required")
