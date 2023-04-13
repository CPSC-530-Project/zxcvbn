To run the program go to hashcat-6.2.6 folder
On windows, type cmd to go to command line.
Type 'python script.py' on command line to run program.
This script runs 2 programs:

1. strength_estimator.py:
1.1 Requires 'pip install zxcvbn'.
1.2 Runs all passwords from dataset '38650-password-sktorrent.txt' in zxcvbn and gets a score for each password-sktorrent.
1.3 Writes 7 output files: 
1.3.a 1 csv file of all the passwords and results from zxcvbn.
1.3.b 1 csv file of the averages by score for zxcvbn results .
1.3.c 5 text files of plain text passwords separated by their score.
1.4 Requires a command line argument 'tot' or 'lt8':
1.4.a 'tot' separates all passwords from '38650-password-sktorrent.txt' by score.
1.4.b 'lt8' separates all passwords less than length 8 from '38650-password-sktorrent.txt' by score.
1.5 The python script runs 'strength_estimator.py' with the command line argument 'tot' first followed by 'lt8'

2. encodeMD5.py
2.1 Takes an input file of passwords and produces an ouput file of the MD5 hashes of those passwords.
2.2 Requires 2 command line arguments for file type (tot/lt8) and the other for score (0-4)
2.3 'script.py' does all of this automatically. At the end, all of the 10 text files for passwords (from 1) are encrypted into MD5.

Next, the script runs 3 hashcat attack types from the command line.
There are 3 boolean values on lines 5-7 to run the attack types.
Currently all values are False. Change them to True to run the attacks.
BruteForce Attack takes about 26 hours
Dictionary Attack takes about 1 minute
Hybrid Attack takes about 3 hours.

The results of all 3 HashCat attacks are stored in the 'Results' folder.
There is also an Excel file called 'Results - Graphs and Tables' that contains all the graphs and tables used in our report.


