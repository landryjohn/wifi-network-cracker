# wifi-network-cracker

**A python program for accessing Wi-Fi network using brute force authentication**

Author: Landry John [https://github.com/landryjohn]

### **INSTALLATION**

------

You have to install Python environment to run that project. 

[1] Install Python and PIP

[2] Clone the project 

> git clone https://github.com/landryjohn/wifi-network-cracker 

[3] Install project requirements

> cd ...\wifi-network-cracker
>
> pip install -r requirements.txt 



### HOW IT WORKS

------

Usage: app.py [-h] [-s] [-w]

Optional arguments:
  -h, --help        show this help message and exit
  -s , --ssid       SSID = Access Point Name
  -w , --wordlist   file list of passwords

I used [**pywifi**](https://github.com/awkman/pywifi/blob/master/DOC.md) module that enable interaction with Wi-Fi interfaces. 

TODO : 

- [x] Test the App ✅✅✅
- [x] Write documentation with demo
- [ ] Clean the wordlist according to most Wi-Fi settings (password length > 6)
- [ ] Code Refractory 😪
- [ ] Add other technichs to crack the password 
