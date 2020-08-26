#!/usr/bin/env 

import requests as req
from bs4 import BeautifulSoup
import hashlib

#Prompt for entering website
webpage = input("Enter full website starting with https://www.: ")

#Grab website content
resp = req.get(webpage)
body = BeautifulSoup(resp.text, 'html.parser').find('body')

#Create file to hold contents of webpage
f = open("body.txt", "w")
f.write(str(body))
f.close()

#Generate checksum of webpage.txt
md5_hash = hashlib.md5()

hashfile = open("body.txt",  "rb")
checksum  = hashfile.read()
md5_hash.update(checksum)

cs = md5_hash.hexdigest()

#Create second file containing checksum of webpage.txt
f = open("checksum.txt", "w")
f.write(cs)
f.close()

#Outputting html from website to terminal
print("The body of the webpage has been saved in body.txt")
print("The checksum of body.txt is stored in checksum.txt")
print("Check your current directory for the files")
