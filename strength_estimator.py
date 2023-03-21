from zxcvbn import zxcvbn

INPUTFILE = "passwords.csv"
OUTPUTFILE = "password_strength2.csv"

passwordfile = open("1000000-password-seclists.txt","r")
passwordlist = []
passworddict = {}
#store password in passwordict
for line in passwordfile:
    if len(line) <= 8:
        passwordlist.append(line.strip())
    

#run passwords in zxcvbn() function 
#then store important values into dict
print("running passwords through zxcvbn() function...")
for pw in passwordlist:
    password = zxcvbn(pw)
   
    passworddict[pw] = [password["score"],int(password["guesses"]),password["sequence"][0]["pattern"],float(password["crack_times_seconds"]["offline_fast_hashing_1e10_per_second"]),float(password["crack_times_seconds"]["offline_slow_hashing_1e4_per_second"]),float(password["crack_times_seconds"]["online_no_throttling_10_per_second"]),float(password["crack_times_seconds"]["online_throttling_100_per_hour"])]


newfile = open(OUTPUTFILE,"w+")
#write to csv file
for pw in passworddict:
    newfile.write(f"{pw},{passworddict[pw][0]},{passworddict[pw][1]},{passworddict[pw][2]},{passworddict[pw][3]},{passworddict[pw][4]},{passworddict[pw][5]},{passworddict[pw][6]}\n")

passwordfile.close()
newfile.close()