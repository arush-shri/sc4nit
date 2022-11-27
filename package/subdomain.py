#!/usr/bin/python

import requests
import pyfiglet
import random
import threading
from termcolor import colored

def request(url):

	try:
		return requests.get("http://" + url, timeout=1)
	except requests.exceptions.ConnectionError:
		pass

def banner():
	fonts = ["banner","big","bubble","digital","emboss","emboss2","future","letter","mini","pagga","script","shadow","slant","small","smblock"]
	ran_font = random.choice(fonts)
	colors = ["grey","red","green","yellow","blue","magenta","cyan","white"]
	ran_color = random.choice(colors)
	banner = pyfiglet.figlet_format("SUBDOMAIN\nFINDER",font = ran_font)
	print (colored(banner, ran_color))

def main():
	target = input("[*] Target Domain: ")

	file = open("package/subdomains.txt", "r")

	for line in file:
		try:
			word = line.strip()
			full_url = word + "." + target
			response = request(full_url)
			if response:
				print (colored("[+] Discovered subdomain: " + full_url, 'green'))
		except:
			return()


