####################################
####################################
from time import sleep as timeout
import time
import base64
import socket
import sys
import os
#try:
os.system('clear')
####################################
def restart () :
    os.system('clear')
    print (' ')
    bnn ()
    print (' ')
    print (' ')
    print (' ')
    print (' ')
    print (' ')
    print (' ')
    print ("\033[1;31m                 ╔╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╗")
    print ("\033[1;31m                 ╢                         ╢")
    print ("\033[1;31m                 ╢\033[1;33m    Back To Main ...?   \033[1;31m ╢")
    print ("\033[1;31m                 ╢                         ╢")
    print ("\033[1;31m                 ╚╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╝")
    print (' ')
    print (' ')
    restart = input ('\033[1;32m ~  Press Enter To Continue:  ')
    if restart == '' :
        os.system('clear')
        v7x_banner ()
        home_main ()
