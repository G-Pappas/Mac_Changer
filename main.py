#!/usr/bin/env Python
import subprocess


def ask_for_input():
    # Ask user which interface he want to interact with.
    ask_for_input.inter_name = str(input("Enter interface name to interact:\n "))
    # Ask user for mac address.
    ask_for_input.new_mac = str(input("Enter new mac address:\n "))


# Function to change the mac address.
def change_mac():
    # Turn the interface I want to interact with down.
    subprocess.call(["ifconfig", ask_for_input.inter_name, "down"])
    # Change mac.
    subprocess.call(["ifconfig", ask_for_input.inter_name, "hw", "ether", ask_for_input.new_mac])
    # After making the changes I want turn the interface up again.
    subprocess.call(["ifconfig", ask_for_input.inter_name, "up"])


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
