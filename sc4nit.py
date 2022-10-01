#! /usr/bin/python3

from package import port_scanner
from package import subdomain

from termcolor import colored
import os
import pyfiglet
import random

__version__ = "1.2.1"

fonts = ["banner","big","bubble","digital","emboss","emboss2","future","letter","mini","pagga","script","shadow","slant","small","smblock"]
ran_font = random.choice(fonts)
colors = ["grey","red","green","yellow","blue","magenta","cyan","white"]
ran_color = random.choice(colors)

def banner():
	banner = pyfiglet.figlet_format("SC4N!T",font = ran_font)
	print (colored(banner, ran_color))
	print (colored("version: " + __version__, ran_color))

def choose():
	print ("\n\n1.Subdomains finder\n2.Port Scanner\n3.Exit")
	choice = input()
	if (choice == "1"):
		os.system("clear")
		subdomain.banner()
		subdomain.main()
		choose()
	if (choice == "2"):
		os.system("clear")
		port_scanner.banner()
		port_scanner.main()
		choose()
	if (choice == "3"):
		exit()

os.system("clear")
banner()
choose()
