#!/usr/bin/env python

import subprocess
import optparse


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + "to " + new_mac)

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="The Interface that you want to change the MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="MAC address you want to change to")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please enter the interface")
    elif not options.new_mac:
        parser.error("Please enter MAC address")
    return options


options = get_arguments()

change_mac(options.interface, options.new_mac)

# subprocess.call("sudo ifconfig eth0 down", shell=True)
# subprocess.call("sudo ifconfig eth0 hw ether 00:11:22:33:44:55", shell=True)
# subprocess.call("sudo ifconfig eth0 up", shell=True)
