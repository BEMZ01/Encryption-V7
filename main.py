import encrypto as enc
print(enc.getkey("f"))
print(enc.encrypt(input("Text to encrypt.\n>>>: ")))
print(enc.decrypt("message.enc", "key.enc"))
print(enc.generate_frame())
print("Generated random frame from last 5 sec")