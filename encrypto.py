import requests
import random
from datetime import datetime
from PIL import Image
import re
import os
import string

def getkey(string):
  '''
  RUN AFTER generate_frame()
  Generate a radom key using random objects
  '''
  temp = 0
  for x in range(0, len(string)):
    inpt = ord(str(string[x]))
    t = int(re.sub("[^0-9]", "", str(datetime.now())))
    requests.get(generate_frame())
    im = Image.open("temp_frame.jpeg")
    width, height = im.size
    r, g, b = im.getpixel((random.randint(0, width),random.randint(0, height)))
    os.remove('temp_frame.jpeg')
    temp = temp + (inpt * (r+b+g))
    temp += t
  temp = hex(int(temp))
  return(temp)

def encrypt(text):
  '''
  Convert text to encrypted text, stores message and key to message.enc and key.enc respectivley. Returns tuple containing message and key.
  '''
  fin = ""
  key = int(getkey(random.choice(string.ascii_letters)), 0)
  for x in range(0, len(text)):
    texttemp = ord(text[x])
    texttemp += key
    fin += ":"+str(texttemp)
  message = open("message.enc", "w+")
  message.write(fin[1:])
  message.close()
  enc = open("key.enc", "w+")
  enc.write(str(key))
  enc.close()
  return(str(fin[1:]), key)

def decrypt(path_to_message, path_to_key):
  '''
  Open the key and message file, then decrypt the message.
  '''
  tempa = []
  message = open(path_to_message, "r")
  message = message.readlines()[0]
  key = open(path_to_key, "r")
  key = int(key.readlines()[0])
  message = message.split(":")
  for x in range(0, len(message)):
    temp = int(message[x])
    temp -= key
    temp = chr(temp)
    tempa.append(temp)
  fin = ''.join([str(elem) for elem in tempa]) 
  return(fin)

def generate_frame():
  '''
  Download and save a random frame from online webcam
  Returns base URL
  '''
  url = "http://109.233.191.130:8080/cam_4.jpg?uniq="
  fin = "0."
  for x in range(0, 15):
    fin = fin + str(random.randint(0, 9))
  url = url + str(fin)
  f = requests.get(url)
  file = open("temp_frame.jpeg", "wb")
  file.write(f.content)
  file.close()
  return(url)