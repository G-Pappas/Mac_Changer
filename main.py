#!/usr/bin/env Python
import subprocess
import re


def ask_for_input():
    # Ask user which interface he want to interact with.
    user_interface_input = str(input("Enter interface name to interact:\n "))

    # Check if the interface user added exists.
    interface_check = re.search(r"\w\w\w\w", user_interface_input)
    if interface_check:
        ask_for_input.inter_name = user_interface_input
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~Interface is wrong, please try again.~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        ask_for_input()

    # Ask user for mac address.
    user_mac_input = str(input("Enter new mac address:\n "))

    # Check if MAC address has a valid format.
    mac_check = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", user_mac_input)
    if mac_check:
        ask_for_input.new_mac = user_mac_input
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~Wrong MAC Address format, please try again.~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Function to change the mac address.
def change_mac():
    # Turn the interface I want to interact with down.
    subprocess.call(["ifconfig", ask_for_input.inter_name, "down"])
    # Change mac.
    subprocess.call(["ifconfig", ask_for_input.inter_name, "hw", "ether", ask_for_input.new_mac])
    # After making the changes I want turn the interface up again.
    subprocess.call(["ifconfig", ask_for_input.inter_name, "up"])


# Print new mac address to the user
def print_new_mac():
    ifconfig_result = subprocess.check_output(["ifconfig"])
    my_new_mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    print("MAC address successfully changed to: ", my_new_mac_address.group(0))


# Function to reset mac value to default state.
def reset_mac():
    subprocess.call("ifconfig eth0 down", shell = True)
    subprocess.call("ifconfig eth0 up", shell = True)
    subprocess.call("sudo ifconfig eth0 hw ether $(ethtool -P eth0 | awk '{print $3}')", shell = True)
    subprocess.call("ifconfig eth0 down", shell = True)
    subprocess.call("ifconfig eth0 up", shell = True)


# Function to browse in the program.
def user_greet():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("To change mac address press 1")
    print("To reset default mac value press 2")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    user_choice = input()
    if user_choice == "1":
        ask_for_input()
        change_mac()
        print_new_mac()
    elif user_choice == "2":
        reset_mac()
    else:
        print("\n")
        print("\n")
        print("************************************")
        print("*    Please chose option 1 or 2    *")
        print("************************************")
        user_greet()


user_greet()
