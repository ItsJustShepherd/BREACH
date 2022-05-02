#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports.
from os import system, name

# Main logo.
def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
