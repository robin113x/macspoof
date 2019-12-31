#!/usr/bin/evn python
#import pyfiglet
import subprocess
import optparse
parse = optparse.OptionParser()
#b_b = pyfiglet.figlet_format("\nMAC  CHANGER")
#print(b_b)
print("\t\t\t\t\t\t\t\t-Robin\n")
face = raw_input("\nEnter the Network Interface(wlan0/eth0) = ")
if not face:
    parse.error("[-] please specify your interface i.e wlan0 or eth0")
mc = raw_input("\nEnter new MAC Address (Ex xx:xx:xx:xx:xx:xx) = ")
if not mc:
    parse.error("[-] please Enter New MAC ADDRESS")
print("\n************************************************************")
print("MAC Address of network interface " + face + "change to " + mc)
print("************************************************************\n")
subprocess.call(["ifconfig", face, "down"])
subprocess.call(["ifconfig", face, "hw", "ether", mc])
subprocess.call(["ifconfig", face, "up"])
subprocess.call(["ifconfig", face])

