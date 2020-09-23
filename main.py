#!/usr/bin/env Python

import subprocess

# Ask user which interface he want to interact with.
int_name = input("Enter interface name to interact:\n ")
# Ask user for mac address.
new_mac = input("Enter new mac address:\n ")


def change_mac():
    # Turn the interface I want to interact with down.
    subprocess.call(f'ifconfig {int_name} down', shell = True)
    # Change mac.
    subprocess.call(f'ifconfig {int_name} hw ether {new_mac}', shell = True)
    # After making the changes I want turn the interface up again.
    subprocess.call(f'ifconfig {int_name} up', shell = True)


change_mac()
