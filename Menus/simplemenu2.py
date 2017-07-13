#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Title: simplemenu.py
# Description: Displays a simple menu, with sub menus. 
# Author: Nick
# Date: 13/07/17
# Usage: python simplemenu.py
# Python version: 2.7
#===================================================================

# Import modules
import sys, os

# Constants
menu_actions = {}

# Menu functions


# Main menu
def main_menu():
    os.system('clear')
    print "Welcome, \n"
    print "Please choose menu: "
    print "1) Menu 1"
    print "2) Menu 2"
    print "\n0) Quit"
    choice = raw_input(" >> ")
    exec_menu(choice)

# execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return

# Menu 1
def menu1():
    print "Hello menu 1 !\n"
    print "9) Back"
    print "0) Quit"
    choice = raw_input(" >> ")
    exec_menu(choice)
    return


# Menu 2
def menu2():
    print "Hello menu 2 !\n"
    print "9) Back"
    print "0) Quit"
    choice = raw_input(" >> ")
    exec_menu(choice)
    return

# Back to main menu
def back():
    menu_actions['main menu']()

# Exit program
def exit():
    sys.exit()


# Menus definition
menu_actions = {
        'main_menu': main_menu,
        '1': menu1,
        '2': menu2,
        '9': back,
        '0': exit,
}

# Main program
if __name__ == "__main__":
    main_menu()


