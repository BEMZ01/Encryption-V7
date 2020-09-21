import encrypto as enc
print(enc.getkey("f")) # generate a random key, requires a string lenth of > 1
print(enc.encrypt(input("Text to encrypt.\n>>>: "))) # encrypt some text, returns tuple (message, key) also writes to message.enc and key.enc
print(enc.decrypt("message.enc", "key.enc")) # decrypt message using files. Returns plaintext.
print(enc.generate_frame()) # generate a frame from the webcam
print("Generated random frame from last 5 sec")