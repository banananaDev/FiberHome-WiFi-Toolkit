
import os
import sys

from modules.password_generator import generate_password
from modules.password_checker import check_password
from modules.mac_info import format_mac
from modules.ont_info import show_ont_info
from modules.password_history import (
    save_password,
    show_history,
    export_history
)

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
WHITE = "\033[97m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def clear():
    os.system("clear")

def banner():
    print(CYAN + r"""
  _____ _ _               _   _
 |  ___(_) |__   ___ _ __| | | | ___  _ __ ___   ___
 | |_  | | '_ \ / _ \ '__| |_| |/ _ \| '_ ` _ \ / _ \
 |  _| | | |_) |  __/ |  |  _  | (_) | | | | | |  __/
 |_|   |_|_.__/ \___|_|  |_| |_|\___/|_| |_| |_|\___|

             WIFI TOOLKIT
""" + RESET)

    print(YELLOW + "       FIBERHOME NETWORK UTILITIES" + RESET)
    print(WHITE + "       Version 1.1.0 | Advanced Edition" + RESET)
    print("-" * 55)

def menu():
    print(f"""
{GREEN}[1]{WHITE} Generate WiFi Password
{GREEN}[2]{WHITE} Password Strength Checker
{GREEN}[3]{WHITE} MAC Address Formatter
{GREEN}[4]{WHITE} ONT Information
{GREEN}[5]{WHITE} Password History
{GREEN}[6]{WHITE} Export History TXT
{GREEN}[0]{WHITE} Exit
""")

def main():
    while True:
        clear()
        banner()
        menu()

        choice = input(f"{CYAN}root@fiberhome ~ # {RESET}").strip()

        if choice == "1":
            try:
                length = input("Password length (8-63, default 12): ").strip()
                length = int(length) if length else 12

                password = generate_password(length)

                print(f"\n{GREEN}[+] Generated: {password}{RESET}")

                save = input("Save to history? (y/n): ").lower()

                if save == "y":
                    save_password(password)
                    print(f"{GREEN}[+] Password saved!{RESET}")

            except ValueError as error:
                print(f"{RED}[ERROR] {error}{RESET}")

        elif choice == "2":
            password = input("Enter password: ")
            print(check_password(password))

        elif choice == "3":
            mac = input("Enter MAC address: ")
            print(format_mac(mac))

        elif choice == "4":
            show_ont_info()

        elif choice == "5":
            print("\n" + show_history())

        elif choice == "6":
            print(export_history())

        elif choice == "0":
            print("Exiting FiberHome Toolkit...")
            sys.exit(0)

        else:
            print(f"{RED}Invalid menu!{RESET}")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
