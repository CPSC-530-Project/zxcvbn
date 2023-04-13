import sys

if (len(sys.argv) != 3):
    sys.exit("Need a FileType Argument + Score Number")
if ((sys.argv[1] != "tot") and (sys.argv[1] != "lt8")):
    sys.exit("Wrong FileType Argument [tot/lt8]")
if(int(sys.argv[2]) < 0 or int(sys.argv[2]) > 4):
    sys.exit("Score Number must be between 0 and 4")

INFILE = "38650-password-sktorrent-" + sys.argv[1] + "-s" + sys.argv[2] + ".txt"
newfile = open(INFILE, "r")

passwordList = []
i1 = i2 = i3 = i4 = i5 = i6 = i7 = i8 = i8p = 0
for line in newfile:
    pw = line.strip()
    if(len(pw) > 0): 
        passwordList.append(pw)

for pw in passwordList:
    if(len(pw) == 1):
        i1 += 1
    if(len(pw) == 2):
        i2 += 1
    if(len(pw) == 3):
        i3 += 1
    if(len(pw) == 4):
        i4 += 1
    if(len(pw) == 5):
        i5 += 1
    if(len(pw) == 6):
        i6 += 1
    if(len(pw) == 7):
        i7 += 1
    if(len(pw) == 8):
        i8 += 1
    if(len(pw) > 8):
        i8p += 1

print("-------------- Word Distribution of " + INFILE + " --------------")
print("Length 1: " + str(i1))
print("Length 2: " + str(i2))
print("Length 3: " + str(i3))
print("Length 4: " + str(i4))
print("Length 5: " + str(i5))
print("Length 6: " + str(i6))
print("Length 7: " + str(i7))
print("Length 8: " + str(i8))
print("Length 8+: " + str(i8p))
print("-----------------------------------------------------------------")

newfile.close()