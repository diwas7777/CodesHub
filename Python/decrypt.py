#this project is the decryption algorithm for ransomware.py
import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "key.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print (files, "\n\n")

with open("key.key", "rb") as thekey:
    secretKey = thekey.read()

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretKey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
