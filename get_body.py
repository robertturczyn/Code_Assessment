#!/usr/bin/env 

import requests as req
from bs4 import BeautifulSoup
import os

#Prompt for entering website
webpage = input("Enter full website starting with https://www.: ")
body = "null"

#Grab website content
resp = req.get(webpage)

#Populate entire html body or just the text of the body
def my_choice(body):
  choice = input("Press 1 for just text of body or select 2 for full html drop of body: ")
  choice = int(choice)
  if choice == 1:
    body = BeautifulSoup(resp.text, 'html.parser').find_all('body')[0].get_text()
  elif choice == 2:
   body = BeautifulSoup(resp.text, 'html.parser').find('body')
  else:
    print("Please select either 1 or 2")
    my_choice(body)
  return str(body)

#Create file to hold contents of webpage
f = open("body.txt", "w")
f.write(my_choice(body))
f.close()

def sh(checksum):
  os.system("bash -c '%s'" % checksum)

sh("cksum body.txt > checksum.txt")

#Outputting html from website to terminal
print("The body of the webpage has been saved in body.txt")
print("The checksum of body.txt is stored in checksum.txt")
print("Check your current directory for the files")
