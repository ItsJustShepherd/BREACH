#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys # System stuff.
import os # Operating System functions.
import time # Time.
import subprocess # Now with extra cookies!
import requests # For making requests.
import json # Make those sweet JSON files.
import argparse # Google said I needed this.
import core.breach_logo as logo # My logo, of course.
import core.colors as colors # We all love a splash of color.
import core.mods as mods # So we can let people modify it easier!

def main():

    # Imports.
    import sys # System stuff.
    import os # Operating System functions.
    import time # Time.
    import subprocess # Now with extra cookies!
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
    ap.add_argument('-fallenflare', help='Attempts to bypass cloudflare due to misconfigurations in CNAME, MX, TXT.\n', action='store_true') # Working.
    ap.add_argument('-gitinfo', help='Pulls a list of users repositories.\n', action='store_true') # Working.
    ap.add_argument('-gitreaper', help='Pulls potential name/email(s) from git commit history+forks.\n', action='store_true') # Working.
    #ap.add_argument('-portscan', help='Scan a range of ports!\n', action='store_true') # Developing.
    # ap.add_argument('-vulncheck', help='Scan for Log4j, heartbleed, etc!\n', action='store_true') # Developing.
    # ap.add_argument('-phone', help='Phone lookup, etc.\n', action='store_true') # Further research needed.
    # ap.add_argument('-email', help='Email lookup, etc.\n', action='store_true') # Further research needed.
    # ap.add_argument('-u', '-update', help='Pulls the latest update from github.\n', action='store_true') # Developing.
    # ap.add_argument('-setup', help='Installs everything you need to run breach.\n', action='store_true') # Developing.
    ap.add_argument('-v', '-version', help='Version, nothing more or less.\n', action="version", version='ALPHA x.2.2') # Working.
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
            print("") # Adds a break in the lines.
            if  tor == "yes":
                os.system("sudo apt install tor -y")
                print("Tor is now installed.\n")
                break # Stops any loops.
            elif    tor == "no":
                print("Tor has not been installed. \n")
            break # Stops any loops.

    # Tor.
    if args['tor']:
        mods.clear_screen() # Clears the screen.
        logo.breach_logo() # Prints the logo.
        while True:
            tor = input("Tor controller | on/off/reload: >_ ") # The Tor controller.
            print("") # Adds a break in the lines.
            if  tor == "on":
                os.system("sudo service tor start")
                print("Tor is now online.\n")
                break # Stops any loops.
            elif    tor == "off":
                os.system("sudo service tor stop")
                print("Tor is now offline.\n")
                break # Stops any loops.
            elif    tor == "reload":
                os.system("sudo service tor restart")
                print("Tor has been restarted.\n")
            break # Stops any loops.

    # Ping.
    if args['ping']:
        mods.clear_screen() # Clears the screen.
        logo.breach_logo() # Prints the logo.
        while True:
            ip_address = input("\nPlease enter the ip/domain address that you want to ping: >_ ") # Just asks you to give the program what IP you want to ping.
            print("") # Adds a break in the lines.
            print(f"IP/Domain: {ip_address}, is about to be pinged!\n") # Let's you know the IP was accepted for use.
            break # Stops any loops.
        while True:
            os.system(f"ping {ip_address} -c 3\n") # Pings it 3x.
            break # Stops any loops.

    # Whois.
    if args['whois']:
        mods.clear_screen() # Clears the screen.
        logo.breach_logo() # Prints the logo.
        while True:
            ip_address = input("\nEnter the ip/domain: >_ ") # Just asks you to give the program what IP you want to whois.
            print("") # Adds a break in the lines.
            print(f"IP/Domain: {ip_address}, locking on!\n") # Let's you know the IP was accepted for use.
            os.system(f"traceroute {ip_address}\n") # trace routes the IP
            os.system(f"whois {ip_address} -H\n") # whois request grabs.
            break # Stops any loops.

    # Fallenflare.
    if args['fallenflare']:
        mods.clear_screen() # Clears the screen.
        logo.breach_logo() # Prints the logo.
        while True:
            try:
                print("Ignore any 'rm' attempts if shown:")
                os.system(f"rm /tmp/nslookup_cname") # Removes nslookup_cname if one exits.
                os.system(f"rm /tmp/nslookup_mx") # Removes nslookup_mx if one exits.
                os.system(f"rm /tmp/nslookup_txt") # Removes nslookup_txt if one exits.
                os.system(f"rm /tmp/fallenflare_result_ping") # Removes the results.
                os.system(f"rm /tmp/fallenflare_result_whois") # Removes the results.
                print("") # Adds a break in the lines.
                ip_address = input("\nEnter the ip/domain: >_ ") # Just asks you to give the program what IP you want to look into.
                print("(If you want to stop checks use 'ctrl+c')\n")
                time.sleep(2)  # Change load times by changing this, if you make it to fast it can mess up ordering!
                print(f"Checking: {ip_address} please wait a moment.\n") # Let's you know the IP was accepted for use.
                os.system(f"nslookup -query=cname {ip_address} >> /tmp/nslookup_cname\n") # runs nslookup CNAME.
                os.system(f"nslookup -query=mx {ip_address} >> /tmp/nslookup_mx\n") # runs nslookup MX.
                os.system(f"nslookup -query=txt {ip_address} >> /tmp/nslookup_txt\n") # runs nslookup TXT.
                os.system(f"echo {ip_address} && sed -n '/origin/,$p' /tmp/nslookup_cname | head -1\n") # Lets you know if MX existed.
                os.system(f"sed -n '/mail addr/,$p' /tmp/nslookup_cname | head -1\n") # Lets you know if MX existed.
                print("") # Adds a break in the lines.
                os.system(f"sed -n '/exchanger/,$p' /tmp/nslookup_mx | head -1\n") # Lets you know if MX existed.
                print("") # Adds a break in the lines.
                os.system(f"sed -n '/text/,$p' /tmp/nslookup_txt | head -1\n") # Lets you know if MX existed.
                print("") # Adds a break in the lines.
                ip_address = input("Enter any given cname, mx or txt ip/domain: >_ ") # Just asks you to give the program what IP you want to follow up.
                print(f"\nIP/Domain: {ip_address}, locking on!\n") # Let's you know the IP was accepted for use.
                os.system(f"ping -c 1 {ip_address} >> /tmp/fallenflare_result_ping") # Prints out the fallenflare ping result to be later cat'd.
                os.system(f"whois {ip_address} -H >> /tmp/fallenflare_result_whois") # Prints out the fallenflare whois result to be later cat'd.
                print("Potential match for source IP/Domain:")
                os.system("cat /tmp/fallenflare_result_whois") # Cats the fallenflare whois result.
                os.system("cat /tmp/fallenflare_result_ping | head -1") # Cats the fallenflare ping result.
                sys.exit(0)
            except KeyboardInterrupt:
                os.system(f"rm /tmp/nslookup_cname") # Removes nslookup_cname if one exits.
                os.system(f"rm /tmp/nslookup_mx") # Removes nslookup_mx if one exits.
                os.system(f"rm /tmp/nslookup_txt") # Removes nslookup_txt if one exits.
                os.system(f"rm /tmp/fallenflare_result_ping") # Removes the results.
                os.system(f"rm /tmp/fallenflare_result_whois") # Removes the results.
                print('\nYou interrupted the program.')
                try:
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)

    # Gitinfo.
    if args['gitinfo']:
        mods.clear_screen() # Clears the screen.
        logo.breach_logo() # Prints the logo.
        while True:
            print("") # Adds a break in the lines..
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
                        name = data2[j]['commit']['author']['name'] # Name data to data2.
                        email = data2[j]['commit']['author']['email'] # Email data to data2.
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
            print("The boot test successful.") # Adds a break in the lines.
            os.system("python3 ./breach.py -v")
            break # Stops any loops.

    ## Template.
    #if args['template-name']:
    #    mods.clear_screen() # Clears the screen.
    #    logo.breach_logo() # Prints the logo.
    #    while True:
    #        def template_run():
    #        print("script goes here.") # Adds a break in the lines..
    #        break # Stops any loops.
    #    else :
    #        exit()

if __name__ == '__main__':
    import sys # System stuff.
    import os # Operating System functions.
    try:
        main()
    except KeyboardInterrupt:
        print('\nYou interrupted the program.')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)