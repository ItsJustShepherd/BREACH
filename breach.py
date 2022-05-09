#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports.
import os # Operating System functions.
import time # Time.
import requests # For making requests.
import json # Make those sweet JSON files.
import argparse # Google said I needed this.
import core.breach_logo as logo # My logo, of course.
import core.colors as colors # We all love a splash of color.
import core.mods as mods # So we can let people modify it easier!

# List of commands.
parser = argparse.ArgumentParser()
ap = parser.add_mutually_exclusive_group()
ap.add_argument('-tor_install', help='Install Tor onto the device.\n', action="store_true") # Working (Sudo or PrivEsc needed).
ap.add_argument('-tor', help='Utilise the Tor network.\n', action="store_true") # Working.
ap.add_argument('-ping', help='Send a customisable ping.\n', action='store_true') # Working.
ap.add_argument('-whois', help='Easy to read domains lookup, nameservers, etc with no ICANN.\n', action='store_true') # Working.
ap.add_argument('-gitinfo', help='Pulls a list of users repositories.\n', action='store_true') # Working.
ap.add_argument('-gitreaper', help='Pulls potential name/email(s) from git commit history+forks.\n', action='store_true') # Working.
#ap.add_argument('-portscan', help='Scan a range of ports!\n', action='store_true') # Developing.
# ap.add_argument('-vulncheck', help='Scan for Log4j, heartbleed, etc!\n', action='store_true') # Developing.
# ap.add_argument('-phone', help='Phone lookup, etc.\n', action='store_true') # Further research needed.
# ap.add_argument('-email', help='Email lookup, etc.\n', action='store_true') # Further research needed.
# ap.add_argument('-u', '-update', help='Pulls the latest update from github.\n', action='store_true') # Developing.
# ap.add_argument('-setup', help='Installs everything you need to run breach.\n', action='store_true') # Developing.
ap.add_argument('-v', '-version', help='Version, nothing more or less.\n', action="version", version='ALPHA x.2.x') # Working.
ap.add_argument('-contributors', help='Cats the contributors file.\n', action='store_true') # Working.
ap.add_argument('-boottest', help='Runs the boot test.\n', action="store_true") # Working.

args = vars(parser.parse_args())

# Fair warning notice before it runs.
notice = f'''
#  {colors.bcolors.RED}Please read the following information carefully before using this tool:{colors.bcolors.ENDC}
#  The content of the this repository is for educational purposes and uses only, or in a professional capacity.{colors.bcolors.ENDC}
'''

# Tor_install.
if args['tor_install']:
    mods.clear_screen() # Clears the screen.
    logo.breach_logo() # Prints the logo.
    while True:
        tor = input("Do you want to install Tor? | yes/no: >_") # Asks if you've got Tor services installed.
        print("\n") # Adds a break in the lines
        if  tor == "yes":
            os.system("sudo apt install tor -y")
            print("Tor is now installed.\n")
            break
        elif    tor == "no":
            print("Tor has not been installed. \n")
        break # Stops any loops.

# Tor.
if args['tor']:
    mods.clear_screen() # Clears the screen.
    logo.breach_logo() # Prints the logo.
    while True:
        tor = input("Tor controller | on/off/reload: >_ ") # The Tor controller.
        print("\n") # Adds a break in the lines
        if  tor == "on":
            os.system("sudo service tor start")
            print("Tor is now online.\n")
            break
        elif    tor == "off":
            os.system("sudo service tor stop")
            print("Tor is now offline.\n")
            break
        elif    tor == "reload":
            os.system("sudo service tor restart")
            print("Tor has been restarted.\n")
        break # Stops any loops.

# Ping.
if args['ping']:
    mods.clear_screen() # Clears the screen.
    logo.breach_logo() # Prints the logo.
    while True:
        pingreq_ip_entered = input("\nPlease enter the ip address that you want to ping: >_ ") # Just asks you to give the program what IP you want to ping.
        print("\n") # Adds a break in the lines
        print(f"IP/Domain: {pingreq_ip_entered}, is about to be pinged!\n") # Let's you know the IP was accepted for use.
        break
    while True:
        os.system(f"ping {pingreq_ip_entered} -c 3\n") # Pings it 3x.
        break # Stops any loops.

# Whois.
if args['whois']:
    mods.clear_screen() # Clears the screen.
    logo.breach_logo() # Prints the logo.
    while True:
        whoisrec_ip_entered = input("Please enter the ip address that you want to record grab and check: >_ ") # Just asks you to give the program what IP you want to whois.
        print("\n") # Adds a break in the lines
        print(f"IP/Domain: {whoisrec_ip_entered}, locking on!\n") # Let's you know the IP was accepted for use.
        os.system(f"traceroute {whoisrec_ip_entered}\n") # trace routes the IP
        os.system(f"whois {whoisrec_ip_entered} -H\n") # whois request grabs.
        break # Stops any loops.

# Gitinfo.
if args['gitinfo']:
    mods.clear_screen() # Clears the screen.
    logo.breach_logo() # Prints the logo.
    while True:
        print("\n") # Adds a break in the lines
        username = input("GitHub username: >_ ") # Just asks you to give the username from GitHub.
        print(f"Checking: {username} for repos (incl. forks)...\n")
        r = requests.get(f'https://api.github.com/users/{username}/repos') # This does cause rate limiting, but we've found it works well for a handful of 'one-off checks' pulling from the api site.
        data = json.loads( r.text )

        for i in range(len(data)):
            url = data[i]['html_url']
            print(f'• {url}\n') # Prints found repos in a bullet point format.
        break # Stops any loops.

# Gitreaper.
if args['gitreaper']:
    mods.clear_screen() # Clears the screen.
    logo.breach_logo() # Prints the logo.
    while True:
        username = input("GitHub username: >_ ") # Just asks you to give the username from GitHub.
        print("(If you want to stop checks use 'ctrl+c')\n")
        time.sleep(2)  # Change load times by changing this, if you make it to fast it can mess up ordering!
        r = requests.get(f'https://api.github.com/users/{username}/repos')  # This does cause rate limiting, but we've found it works well for a handful of 'one-off checks' pulling from the api site.
        print(f"Checking: {username} against commit histories on GitHub (incl. forks)...\n")
        data = json.loads( r.text )

        emails = []
        for i in range(len(data)):
            repo = data[i]['full_name']
            r2 = requests.get(f'https://api.github.com/repos/{repo}/commits') # This does cause rate limiting, but we've found it works well for a handful of 'one-off checks' pulling from the api site.
            data2 = json.loads( r2.text )
            try:
                for j in range(len(data2)):
                    name = data2[j]['commit']['author']['name'] # name data to data2.
                    email = data2[j]['commit']['author']['email'] # email data to data2.
                    if email in emails:
                        pass
                    else:
                        emails.append(email) # Appends emails.
                        print(f"• Username: {name} \n• Email: {email}\n") # Prints the Username followed by Email in a clean bullet point format.
            except Exception:
                print("Failed to get repo commits | potential rate limiting - try again later.")

# Contributors .md.
if args['contributors']:
    mods.clear_screen() # Clears the screen.
    logo.breach_logo() # Prints the logo.
    while True:
        os.system("cat ./contributors.md") # Cats the contributors file.
        break # Stops any loops.

# Boot testing.
if args['boottest']:
    mods.clear_screen() # Clears the screen.
    logo.breach_logo() # Prints the logo.
    print(notice) # Prints the notice seen above, again, if the screen was cleared.
    while True:
        print("The boot test successful.") # Adds a break in the lines
        os.system("python3 ./breach.py -v")
        break # Stops any loops.

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