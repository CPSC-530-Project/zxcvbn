# importing the required libraries
import hashlib

OUTPUTFILE = "passwords_MD5.csv"

passwordfile = open("38650-password-sktorrent.txt","r")
passwordlist = []
#store password in passwordict
for line in passwordfile:
    if len(line) <= 8:
        passwordlist.append(line.strip())

newfile = open(OUTPUTFILE,"w+")
print("hashing the passwords into MD5...")
#for each password, set the input to be the variable itself, the output to be the hash of the variable, and write the password, its hash, and its length to the
#text file.
for pw in passwordlist:
    inputstring = pw
    outputstring = hashlib.md5(inputstring.encode())
    print(outputstring.hexdigest())
    newfile.write(f"{pw}, {outputstring.hexdigest()}, {len(pw)}\n")

passwordfile.close()
newfile.close()
