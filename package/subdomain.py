#!/usr/bin/python

import requests
import pyfiglet
import random
from termcolor import colored

def request(url):
	global full_url
	try:
		full_url = "http://" + url
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass

def sreq(url):
	global full_url
	try:
		full_url = "https://" + url
		return requests.get("https://" + url)

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

	global full_url

	file = open("package/subdomains.txt", "r")
	for line in file:
		word = line.strip()
		full_url = word + "." + target
		response = request(full_url)
		if response:
			print (colored("[+] Discovered subdomain: " + full_url, 'green'))
		sres = sreq(full_url)
		if sres:
			print ("[+] Discovered subdomain: " + full_url)
