print "Before running the code please make sure you have requests and BeautifulSoup installed"
print "pip neesd to be installed for windows please check how to install that,rest the instructions are as follows"
print "To install requests write pip install requests"
print"To install BeautifulSoup write pip install beautifulsoup4"
print "All commands to be written on terminal or cmd"


print "Press enter to continue"

x=raw_input()

import requests

from bs4 import BeautifulSoup

print "Please enter the URL of the webpage"

url=raw_input()

r=requests.get(url)

soup=BeautifulSoup(r.content)

print soup.prettify()
