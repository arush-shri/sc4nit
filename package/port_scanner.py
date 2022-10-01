#!/usr/bin/python

from socket import *
import pyfiglet
import random
from termcolor import colored

def scanner(ports):
	global host
	global sock
	sock = socket(AF_INET, SOCK_STREAM)
	sock.settimeout(0.5)
	try:
		sock.connect((host, ports))
		print (colored("[+]port " + str(ports) + " open", 'green'))
	except:
		print (colored("[-]port " + str(ports) + " closed", 'red'))

def banner():
	fonts = ["banner","big","bubble","digital","emboss","emboss2","future","letter","mini","pagga","script","shadow","slant","small","smblock"]
	ran_font = random.choice(fonts)
	colors = ["grey","red","green","yellow","blue","magenta","cyan","white"]
	ran_color = random.choice(colors)
	banner = pyfiglet.figlet_format("PORT\nSCAN",font = ran_font)
	print (colored(banner, ran_color))


def main():
	global host
	global sock
	host = input("[*] Enter IP: ")
	port_range = input("[*] Enter range to scan: ")
	port_range = port_range.split(",")

	for ports in range(int(port_range[0]) , int(port_range[1]) + 1):
		scanner(host,ports)

	sock.close()
