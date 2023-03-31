# credits to https://www.the-analytics.club/python-shell-commands I learned about the os module from there
import os

# Open input file of md5 hashes and store hashed values in list
INFILE = "38650-password-sktorrent-lt8-s1-1-md5.txt"
passwordfile = open(INFILE, "r")
passwordlist = []

for line in passwordfile:
    if (len(line.strip()) > 0):
        passwordlist.append(line.strip())

# Overall command line arguments        
EXEC = "hashcat.exe"

MODE = 0    # hash type (ex. md5)
ATTACK = 3  # attack type (ex. bruteforce)
RUNTIME = 5 # stop program execution after x seconds
# SKIP = 0    # Start of passwords to crack            
# LIMIT = 1   # End of passwords to crack            
# INCREMENT_MIN = 1       # Initial length of bruteforce string
# INCREMENT_MAX = 8       # Max length of bruteofrce string

OUTFILE = "cracked-s1.csv"                         # Output of hashed values if they were cracked
OUTFILE_FORMAT = "--outfile-format=1,2,3,4,5,6" # Specifies what values are included in the outfile
SEPARATOR = "-p ,"                              # Makes outfile values comma separated
# INFILE = "md5.txt"                              # File of hashed values that needs to be cracked
MASK_RULES = "?a?a?a?a?a?a?a?a"                 # Defines keyspace for bruteforce attack 
                                                # (?a is all lowercase, uppercase, digit and special keys)

INCREMENT = True        # If true, starts from plaintext 1 and goes up to length of mask rules
POTFILE_DISABLE = True  # If true, doesn't save cracked hashes on computer

# Individaual command line arguments
MODE_CMD = "-m " + str(MODE)
ATTACK_CMD = "-a " + str(ATTACK)
RUNTIME_CMD = "--runtime=" + str(RUNTIME)
# SKIP_CMD = "-s " + str(SKIP)
# LIMIT_CMD = "-l " + str(LIMIT)
# INCREMENT_MIN_CMD = "--increment-min=" + str(INCREMENT_MIN)
# INCREMENT_MAX_CMD = "--increment-max=" + str(INCREMENT_MAX) 
OUTFILE_CMD = "-o " + OUTFILE

# All command line arguments
CMD = " ".join([EXEC, MODE_CMD, ATTACK_CMD, OUTFILE_CMD, OUTFILE_FORMAT, SEPARATOR, RUNTIME_CMD]) 

if (INCREMENT):
    CMD += " -i"
if (POTFILE_DISABLE):
    CMD += " --potfile-disable"

for hash in passwordlist:
    # print(str(hash))
    CMD = CMD + " " + str(hash)
    CMD = CMD + " " + MASK_RULES
    # print(CMD)
    directories = os.system(CMD)
    suffix = " " + str(hash) + " " + MASK_RULES
    # print(suffix)
    CMD = CMD.replace(suffix, "")
    # print(CMD)
    
