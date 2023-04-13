from zxcvbn import zxcvbn
import sys

if (len(sys.argv) != 2):
    sys.exit("Need a FileType Argument")
if ((sys.argv[1] != "tot") and (sys.argv[1] != "lt8")):
    sys.exit("Wrong FileType Argument [tot/lt8]")

    
fileType = sys.argv[1]

num0 = num1 = num2 = num3 = num4 = 0
guess0 = guess1 = guess2 = guess3 = guess4 = 0
offh0 = offh1 = offh2 = offh3 = offh4 = 0
ofsh0 = ofsh1 = ofsh2 = ofsh3 = ofsh4 = 0
onn0 = onn1 = onn2 = onn3 = onn4 = 0
ont0 = ont1 = ont2 = ont3 = ont4 = 0

passwordlist = []
passworddict = {}
passwordscore0 = []
passwordscore1 = []
passwordscore2 = []
passwordscore3 = []
passwordscore4 = []
passworddictAvg = {}

IPNUTFILE_NAME = "38650-password-sktorrent"
INPUTFILE = IPNUTFILE_NAME + ".txt"
passwordfile = open(INPUTFILE,"r")

if (sys.argv[1] == "tot"):    
    #store password in passwordict
    for line in passwordfile:
        passwordlist.append(line.strip())
            
if (sys.argv[1] == "lt8"):
    #store password in passwordict
    for line in passwordfile:
        if(len(line) <= 9):
            passwordlist.append(line.strip())
     
OUTPUTFILE = IPNUTFILE_NAME + "-" + fileType + ".csv"
OUTPUTFILE2 = IPNUTFILE_NAME + "-" + fileType + "-avgs.csv"
OUTPUTFILE3 = IPNUTFILE_NAME + "-" + fileType + "-s0" + ".txt"
OUTPUTFILE4 = IPNUTFILE_NAME + "-" + fileType + "-s1" + ".txt"
OUTPUTFILE5 = IPNUTFILE_NAME + "-" + fileType + "-s2" + ".txt"
OUTPUTFILE6 = IPNUTFILE_NAME + "-" + fileType + "-s3" + ".txt"
OUTPUTFILE7 = IPNUTFILE_NAME + "-" + fileType + "-s4" + ".txt"
#run passwords in zxcvbn() function 
#then store important values into dict

i = 0
print("running passwords through zxcvbn() function...")
for pw in passwordlist:
    password = zxcvbn(pw)

    passworddict[pw] = [password["score"],int(password["guesses"]),password["sequence"][0]["pattern"],float(password["crack_times_seconds"]["offline_fast_hashing_1e10_per_second"]),float(password["crack_times_seconds"]["offline_slow_hashing_1e4_per_second"]),float(password["crack_times_seconds"]["online_no_throttling_10_per_second"]),float(password["crack_times_seconds"]["online_throttling_100_per_hour"])]
    if(password["score"] == 0):
        passwordscore0.append(pw)
    if(password["score"] == 1):
        passwordscore1.append(pw)
    if(password["score"] == 2):
        passwordscore2.append(pw)
    if(password["score"] == 3):
        passwordscore3.append(pw)
    if(password["score"] == 4):
        passwordscore4.append(pw)
    if(i % 1000 == 0):
        print(i)
    i += 1

print("Calculate average scores:")
for item in passworddict.items():
    if(item[1][0] == 0):
        num0 += 1
        guess0 += item[1][1]
        offh0 += item[1][3]
        ofsh0 += item[1][4]
        onn0 += item[1][5]
        ont0 += item[1][6]
    elif(item[1][0] == 1):
        num1 += 1
        guess1 += item[1][1]
        offh1 += item[1][3]
        ofsh1 += item[1][4]
        onn1 += item[1][5]
        ont1 += item[1][6]
    elif(item[1][0] == 2):
        num2 += 1
        guess2 += item[1][1]
        offh2 += item[1][3]
        ofsh2 += item[1][4]
        onn2 += item[1][5]
        ont2 += item[1][6]
    elif(item[1][0] == 3):
        num3 += 1
        guess3 += item[1][1]
        offh3 += item[1][3]
        ofsh3 += item[1][4]
        onn3 += item[1][5]
        ont3 += item[1][6]
    elif(item[1][0] == 4):
        num4 += 1
        guess4 += item[1][1]
        offh4 += item[1][3]
        ofsh4 += item[1][4]
        onn4 += item[1][5]
        ont4 += item[1][6]

for i in range(5):
    if (i == 0):
        passworddictAvg[i] = [guess0/num0, offh0/num0, ofsh0/num0, onn0/num0, ont0/num0]
    if (i == 1):
        passworddictAvg[i] = [guess1/num1, offh1/num1, ofsh1/num1, onn1/num1, ont1/num1]
    if (i == 2):
        passworddictAvg[i] = [guess2/num2, offh2/num2, ofsh2/num2, onn2/num2, ont2/num2]
    if (i == 3):
        if (num3 > 0):
            passworddictAvg[i] = [guess3/num3, offh3/num3, ofsh3/num3, onn3/num3, ont3/num3]
        else:
            passworddictAvg[i] = [0,0,0,0,0]
    if (i == 4):
        if(num4 > 0):
            passworddictAvg[i] = [guess4/num4, offh4/num4, ofsh4/num4, onn4/num4, ont4/num4]
        else:
            passworddictAvg[i] = [0,0,0,0,0]

newfile = open(OUTPUTFILE,"w+")
newfile2 = open(OUTPUTFILE2,"w+")
newfile3 = open(OUTPUTFILE3,"w+")
newfile4 = open(OUTPUTFILE4,"w+")
newfile5 = open(OUTPUTFILE5,"w+")
newfile6 = open(OUTPUTFILE6,"w+")
newfile7 = open(OUTPUTFILE7,"w+")

#write to csv file
for pw in passworddict:
    newfile.write(f"{pw},{passworddict[pw][0]},{passworddict[pw][1]},{passworddict[pw][2]},{passworddict[pw][3]},{passworddict[pw][4]},{passworddict[pw][5]},{passworddict[pw][6]}\n")

#write to csv file
for score in passworddictAvg:
    newfile2.write(f"{score},{passworddictAvg[score][0]},{passworddictAvg[score][1]},{passworddictAvg[score][2]},{passworddictAvg[score][3]},{passworddictAvg[score][4]}\n")

#write password to text file by scores
for pw in passwordscore0:
    newfile3.write(f"{pw}\n")
for pw in passwordscore1:
    newfile4.write(f"{pw}\n")
for pw in passwordscore2:
    newfile5.write(f"{pw}\n")
for pw in passwordscore3:
    newfile6.write(f"{pw}\n")
for pw in passwordscore4:
    newfile7.write(f"{pw}\n")

passwordfile.close()
newfile.close()
newfile2.close()
newfile3.close()
newfile4.close()
newfile5.close()
newfile6.close()
newfile7.close()
print("Finished")