SY402_Lab8
Created by Claire Garcia and Ariana McKenzie 
Section 3321 

This repository holds our Lab 8 files

hash.py traverses through all the files on the system, except for the ones we specified
in our inhashable list. It then opens and read each of these files, hashes them, 
and then stores the hash, file path, and date and time in a CSV file. 
It also reads the current filehashes.csv file and then compares that file to what it found while
traversing the file system. It prints out which files were added, which were deleted, and which were 
modified. 
(run program as root, so Python can read all the files on the system) 

filehashes.csv is the output CSV file of hash.py. The first field contains the file path and file name.
The second field contains the hash of the file, and the last field contains the 
date and time.  
 
