# Password Strength Calculator

This script calculates the strength of your password in range from 1 to 10. Checking parameters:
* Password length
* Digits
* Upper- and lowercase letters
* Special symbols (**!@#$%^&\*()[]{}**)
* Is password in blacklist

You can provide your own passwords blacklist as a script parameter. For example, download from here:
[10-million-password-list-top-100](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt)

# How to

Script requires Python 3.5. Example of launch on Linux/Windows:

```bash

$ python password_strength.py blacklist.txt

Password:
Password strength is: 8

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
