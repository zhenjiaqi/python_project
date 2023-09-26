#!/usr/bin/env python

import subprocess
import optparse
import re


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


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("Could not get mac address")


options = get_arguments()
current_mac = get_current_mac(options.interface)

change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
    print("MAC address changed")
else:
    print("MAC did not changed")

# subprocess.call("sudo ifconfig eth0 down", shell=True)
# subprocess.call("sudo ifconfig eth0 hw ether 00:11:22:33:44:55", shell=True)
# subprocess.call("sudo ifconfig eth0 up", shell=True)
