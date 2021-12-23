"""
    Wi-Fi cracker
"""

# Import librairies
import argparse, time, sys, os, platform, re

# Import pywifi librairy
import pywifi
from pywifi import PyWiFi
from pywifi import const
from pywifi import Profile

# Default settings  
ssid="WIFI-NT-SSID"
wordlist="./wordlist.txt"

try: 
    pass 
except Exception as error:
    print("ERROR : " + error)