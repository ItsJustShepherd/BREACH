#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports.
import sys # System.
import time # The time.
import core.cicada_logo as logo # My logo, of course.
import core.cicada_logo_alt as logo_alt # My logo, of course.
import core.colors as colors # We all love a splash of color.
import core.mods as mods # So we can let people modify it easier!

# Start of menu script caller.
def vulncheck():
    def vulncheck_menu():
        global ch
        mods.clear_screen()
        logo.shepherd_logo()

        print(f'''
    CHOOSE OPTION :
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} vulncheck         (Waiting)     [x]
        ''')

        ch = int(input("    --> "))
        print('\n\n')

    vulncheck_menu()

    if ch == 1:
        print('\n Running...\n')
        time.sleep(1)

    elif ch == 2:
        print('\n Running...\n')
        time.sleep(1)

    else:
        print('INVALID OPTION  \n TRY AGAIN')
        sys.exit()