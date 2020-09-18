import encrypto as enc
enc.encrypt("Testing") # Encrypt the string "Testing" (storing files in the Working Directory)
decrypt = enc.decrypt("message.enc", "key.enc") # Decrypt the string "Testing" using the two files created in enc.encrypt
key = enc.getkey("i") # return a random key, requires a string of length > 0 to work. The length directly affects the speed of the key generating.(Note: this does generate a tempory file called temp_frame.jpeg in the Working Directory)
print(key)