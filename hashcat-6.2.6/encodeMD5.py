# importing the required libraries
import hashlib
import sys

if (len(sys.argv) != 3):
    sys.exit("Need a FileType Argument + Score Number")
if ((sys.argv[1] != "tot") and (sys.argv[1] != "lt8")):
    sys.exit("Wrong FileType Argument [tot/lt8]")
if(int(sys.argv[2]) < 0 or int(sys.argv[2]) > 4):
    sys.exit("Score Number must be between 0 and 4")
    
INPUTFILE_NAME = "38650-password-sktorrent-" + sys.argv[1] + "-s" + sys.argv[2] 
INPUTFILE = INPUTFILE_NAME + ".txt"
OUTPUTFILE = INPUTFILE_NAME + "-md5.txt"

passwordfile = open(INPUTFILE,"r")
passwordlist = []
#store password in passwordict
for line in passwordfile:
    if len(line) > 0:
        passwordlist.append(line.strip())

newfile = open(OUTPUTFILE,"w+")
print("hashing the passwords into MD5...")
#for each password, set the input to be the variable itself, the output to be the hash of the variable, and write the password, its hash, and its length to the
#text file.
for pw in passwordlist:
    inputstring = pw
    outputstring = hashlib.md5(inputstring.encode())
    # newfile.write(f"{pw}, {outputstring.hexdigest()}, {len(pw)}\n")
    newfile.write(f"{outputstring.hexdigest()}\n")


passwordfile.close()
newfile.close()
