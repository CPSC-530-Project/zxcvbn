# credits to https://www.the-analytics.club/python-shell-commands I learned about the os module from there
import os

#Attack Type
BRUTE_FORCE = False
DICTIONARY = False
HYBRID = False

#Common Variables
EXEC = "hashcat.exe"
MODE = 0                                        # hash type (0 = md5)
OUTFILE_FORMAT = "--outfile-format=2" # Specifies what values are included in the outfile
SEPARATOR = "-p ,"                              # Makes outfile values comma separated
POTFILE_DISABLE = True                          # If true, doesn't save cracked hashes on computer

MODE_CMD = "-m " + str(MODE)

# BruteForce Variables
RUNTIME = 50                                 # stop program execution after x seconds
RUNTIME_CMD = "--runtime=" + str(RUNTIME)
MASK_RULES = "?a?a?a?a?a?a?a?a"             # Defines keyspace for bruteforce attack (?a is all lowercase, uppercase, digit and special keys)
INCREMENT = True                            # If true, starts from bruteforce for mask of length 1 and goes up to length of mask rules



# Dictionary Variables
dictionaryFolder = "wordlists/"
dictionaryName = "10-million-pw-top1000000"
DICTIONARY_CMD = dictionaryFolder + dictionaryName + ".txt"

# Hybrid Variables
rulesFolder = "hashcatRules/"
rulesName = "OneRuleToRuleThemAll"
RULE_CMD = "-r " + rulesFolder + rulesName + ".rule"


# Run passwords through zxcvbn
fileType = ""
for i in range(2):
  print("------------------------------ Running Passwords Through zxcvbn ------------------------------")
  if (i == 0):
    fileType = "tot"
  else:
    fileType = "lt8"
  STRENGTH_CMD = "python strength_estimator.py " + fileType
  os.system(STRENGTH_CMD)

# Encode passwords to MD5
fileType = ""
for i in range(2):
  print("------------------------------ Encoding Passwords to MD5 ------------------------------")
  if (i == 0):
    fileType = "tot"
  else:
    fileType = "lt8"
  for j in range(5):
    ENCODE_CMD = "python encodeMD5.py " + fileType + " " + str(j)
    #print(ENCODE_CMD)
    os.system(ENCODE_CMD)

if(BRUTE_FORCE):
  # Overall command line arguments        
  ATTACK = 3  # attack type (3 = bruteforce)
  
  print("----------------------------------- BRUTEFORCE ATTACK -----------------------------------")

  for i in range(5):
    # Open input file of md5 hashes and store hashed values in list
    INFILE = "38650-password-sktorrent-lt8-s" + str(i) + "-md5.txt"
    OUTFILE = "cracked-bruteforce-lt8-s" + str(i) + ".txt" # Output of hashed values if they were cracked
  
    passwordfile = open(INFILE, "r")
    passwordlist = []

    for line in passwordfile:
        if (len(line.strip()) > 0):
            passwordlist.append(line.strip())
  
    # Individaual command line arguments
    ATTACK_CMD = "-a " + str(ATTACK)
    OUTFILE_CMD = "-o " + OUTFILE

    # All command line arguments
    CMD = " ".join([EXEC, MODE_CMD, ATTACK_CMD, OUTFILE_CMD, OUTFILE_FORMAT, SEPARATOR, RUNTIME_CMD]) 

    if (INCREMENT):
        CMD += " -i"
    if (POTFILE_DISABLE):
        CMD += " --potfile-disable"

    for pw in passwordlist:
        CMD = CMD + " " + str(pw)
        CMD = CMD + " " + MASK_RULES
        os.system(CMD)
        suffix = " " + str(pw) + " " + MASK_RULES
        CMD = CMD.replace(suffix, "")
if(DICTIONARY):
  print("----------------------------------- DICTIONARY ATTACK -----------------------------------")
  ATTACK = 0  # attack type (ex. 0 = dictionary)
  ATTACK_CMD = "-a " + str(ATTACK)

  for i in range(5):
    # Open input file of md5 hashes and store hashed values in list
    INFILE = "38650-password-sktorrent-tot-s" + str(i) + "-md5.txt"
    OUTFILE = "cracked-dict-" + dictionaryName + "-s" + str(i) + ".txt" # Output of hashed values if they were cracked
    OUTFILE_CMD = "-o " + OUTFILE

    # All command line arguments
    CMD = " ".join([EXEC, MODE_CMD, ATTACK_CMD, INFILE, OUTFILE_CMD, OUTFILE_FORMAT, DICTIONARY_CMD, SEPARATOR]) 
  
    if (POTFILE_DISABLE):
        CMD += " --potfile-disable"

    #print(CMD)
    os.system(CMD)
if(HYBRID):
  print("------------------------------------- HYBRID ATTACK -------------------------------------")
  ATTACK = 0  # attack type (ex. 0 = dictionary)
  ATTACK_CMD = "-a " + str(ATTACK)

  for i in range(5):
    # Open input file of md5 hashes and store hashed values in list
    INFILE = "38650-password-sktorrent-tot-s" + str(i) + "-md5.txt"
    OUTFILE = "cracked-hybrid-" + dictionaryName + "-" + rulesName + "-s" + str(i) + ".txt"  # Output of hashed values if they were cracked
    OUTFILE_CMD = "-o " + OUTFILE

    # All command line arguments
    CMD = " ".join([EXEC, MODE_CMD, ATTACK_CMD, INFILE, OUTFILE_CMD, OUTFILE_FORMAT, DICTIONARY_CMD, RULE_CMD, SEPARATOR]) 
  
    if (POTFILE_DISABLE):
        CMD += " --potfile-disable"

    #print(CMD)
    os.system(CMD)
    
