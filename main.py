import requests
import random
from datetime import datetime
from PIL import Image

def getkey(inp):
  return()
def encrypt():
  return()
def decrypt(inp, key):
  return()

def generate_frame():
  '''
  Download and save a random frame from online webcam
  '''
  url = "http://109.233.191.130:8080/cam_4.jpg?uniq="
  fin = "0."
  for x in range(0, 15):
    fin = fin + str(random.randint(0, 9))
  url = url + str(fin)
  print(url)
  f = requests.get(url)
  file = open("temp_frame.jpeg", "wb")
  file.write(f.content)
  f.close()
  return(url)

req = requests.get(generate_frame())
im = Image.open("temp_frame.jpeg")
width, height = im.size
r, g, b = im.getpixel((random.randint(0, width),random.randint(0, height)))
print(r, g, b)