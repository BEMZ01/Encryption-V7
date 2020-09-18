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
    t = re.sub("[^0-9]", "", str(datetime.now()))
    req = requests.get(generate_frame())
    im = Image.open("temp_frame.jpeg")
    width, height = im.size
    r, g, b = im.getpixel((random.randint(0, width),random.randint(0, height)))
    os.remove('temp_frame.jpeg')
    temp = temp + (inpt * (r+b+g))
  temp = hex(int(temp))
  return(temp)
def encrypt(text, key):
  return()

def decrypt(inp, key):
  return()

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

test = getkey(random.choice(string.ascii_letters))
print(test)