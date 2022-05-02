#!/usr/bin/python
# -*- coding: utf-8 -*-

# Temp note:  Purged and reworked historic records due to major bug.

# Imports.
import sys # System.
import time # The time.
import os # Operating System functions.
import subprocess # So we can call other scripts!
import re # Regular expression, because we all love that... right?
import argparse # Google said I needed this.
import core.breach_logo as logo # My logo, of course.
import core.colors as colors # We all love a splash of color.
import core.mods as mods # So we can let people modify it easier!

# List of commands.
parser = argparse.ArgumentParser()
ap = parser.add_mutually_exclusive_group()
ap.add_argument('-cli', help='Run the Command Line version.\n', action='store_true') # Developing.
ap.add_argument('-ping', help='Send a customised ping.\n', action='store_true') # Working.
ap.add_argument('-gitgrab', help='Given a username, repo and commit I can pull name and emails!\n', action='store_true') # Working.
ap.add_argument('-vulncheck', help='Scan for Log4j, heartbleed, and a port-scanner!\n', action='store_true') # Developing.
ap.add_argument('-whois', help='Domains lookup, nameservers, etc.\n', action='store_true') # Working.
ap.add_argument('-phone', help='Phone lookup, etc.\n', action='store_true') # Further research needed.
ap.add_argument('-email', help='Email lookup, etc.\n', action='store_true') # Further research needed.
ap.add_argument('-vpnc', help='Utilise ProtonVPN through the P-VPN feed option.\n', action="store_true") # Further research needed.
ap.add_argument('-v', '--version', help='Version, nothing more or less.\n', action="version", version='2.5.0') # Working.
ap.add_argument('-boottest', help='Runs the boot test.\n', action="store_true") # Working.
args = vars(parser.parse_args())

# Fair warning notice before it runs.
notice = f'''
#  {colors.bcolors.RED}Please read the following information carefully before using this tool:{colors.bcolors.ENDC}
#  The content of the this repository is for educational purposes and uses only, or in a professional capacity.{colors.bcolors.ENDC} 
# 
#  {colors.bcolors.RED}DO YOU AGREE TO TO OUR TERMS AND CONDITIONS?{colors.bcolors.ENDC} (STATE: Y/N) THEN PRESS "ENTER"
'''

# Start of menu script caller.
def breach_menu():
    global ch
    mods.clear_screen() # Clears the screen.
    logo.breach_logo() # Prints the logo.
    print(f'''
CHOOSE OPTION :
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Ping Request    (Working)     [x]
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Vuln Checking   (Developing)  [x]
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Who Is Record   (Working)     [x]
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} CrypteX         (Waiting)     [x]
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} ProtonVPN Cnct  (Developing)  [x]
    ''')

    ch = int(input("    --> "))
    print('\n\n')

# Boot testing.
if args['boottest']:
    mods.clear_screen() # Clears the screen.
    logo.breach_logo() # Prints the logo.
    print(notice) # Prints the notice seen above, again, if the screen was cleared.
    while True:
        print("The boot test worked.") # Adds a break in the lines
        break
    else :
        sys.exit()

# Ping.
if args['ping']:
    mods.clear_screen() # Clears the screen.
    logo.breach_logo() # Prints the logo.
    while True:
        print("\n") # Adds a break in the lines
        pingreq_ip_entered = input("\nPlease enter the ip address that you want to ping: ") # Just asks you to give the program what IP you want to ping.
        print("\n") # Adds a break in the lines
        print(f"IP/Domain: {pingreq_ip_entered}, is about to be pinged!") # Let's you know the IP was accepted for use.
        print("\n") # Adds a break in the lines
        break
        
    while True:
        os.system(f"ping {pingreq_ip_entered} -c 3") # Pings it 3x.
        print("\n") # Adds a break in the lines
        break # Stops any loops.
    else :  ## MY CODE ##
        sys.exit()

# Gitgrab.
if args['gitgrab']:
    mods.clear_screen() # Clears the screen.
    logo.breach_logo() # Prints the logo.
    while True:
        print("\n") # Adds a break in the lines
        username = input("GitHub username: ") # Just asks you to give the username from GitHub.
        print("\n") # Adds a break in the lines
        repo = input("GitHub Repo name: ") # Just asks you to give the repo name from GitHub.
        print("\n") # Adds a break in the lines
        commit_id = input("GitHub commit_id: ") # Just asks you to give the repo name from GitHub.
        print("\n") # Adds a break in the lines
        os.system(f"wget --output-document=commit.patch --directory-prefix=/tmp https://www.GitHub.com/{username}/{repo}/commit/{commit_id}.patch") # wgets the potentially vulnerable site.
        print("\n") # Adds a break in the lines
        os.system("cd /tmp")
        print("Information found: ")
        print("\n") # Adds a break in the lines
        os.system(f"cat commit.patch | sed '2!d'") # Curls the potentially vulnerable site.
        print("\n") # Adds a break in the lines
        os.system("cd ~")
        print("\n") # Adds a break in the lines
        break # Stops any loops.
    else :
        exit()

# VulnCheck.
#if args['vulncheck']:
#   mods.clear_screen() # Clears the screen.
#   print(notice) # Prints the notice seen above, again, if the screen was cleared.
#        
#    else :
#        sys.exit()

# WhoIs.
if args['whois']:
    mods.clear_screen() # Clears the screen.
    logo.breach_logo() # Prints the logo.
    while True:
        print("\n") # Adds a break in the lines
        whoisrec_ip_entered = input("\nPlease enter the ip address that you want to record grab: ") # Just asks you to give the program what IP you want to whois.
        print("\n") # Adds a break in the lines
        print(f"IP/Domain: {whoisrec_ip_entered}, locking on!") # Let's you know the IP was accepted for use.
        print("\n") # Adds a break in the lines
        os.system(f"traceroute {whoisrec_ip_entered}") # trace routes the IP
        print("\n") # Adds a break in the lines
        os.system(f"whois {whoisrec_ip_entered} -H") # whois request grabs.
        print("\n") # Adds a break in the lines
        break # Stops any loops.
    else :
        sys.exit()

## Template.
#if args['template-name']:
#    mods.clear_screen() # Clears the screen.
#    logo.breach_logo() # Prints the logo.
#    while True:
#        def template_run():
#        print("script goes here.") # Adds a break in the lines.
#        break # Stops any loops.
#    else :
#        exit()

## Main Program (if required).
#if args['cli']:
#    mods.clear_screen()
#    print(notice)
#    yn = input()
#    if yn == 'y' or yn =='Y':
#    print(breach_menu)
#    
#    else :
#        print('YOU MUST AGREE TO THE TERMS BEFORE USE!')
#        exit()
#
#    if ch == 1:
#        print('\nProgram for option 1: \n')
#
#    elif ch == 2:
#        print('\nProgram for option 2: \n')
#
#    elif ch == 3:
#        print('\nProgram for option 3: \n')
#
#    elif ch == x: # Replace 'x' with last number.
#        info.information()
#
#    else:
#        print('INVALID OPTION! \n EXITING.')
#        exit()