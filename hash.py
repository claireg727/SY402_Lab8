
# This code is meant to go through all the files except specified ones

import os               # used for the os.walk() function
import hashlib          # used to hash the files
import csv              # used to create and write to a CSV file 
import datetime         # used to obtain the current time and date

# This is the list of directories not to traverse through
unhashableLst = [
	'/dev',
	'/proc',
	'/run',
	'/sys',
	'/tmp',
	'/var/lib',
	'/var/run'
]

# This list contains each row of the output CSV file where we will store the information
csvRows = {}

# This list will be loaded with data from the previous CSV file
oldCsvData = {}

# open the output CSV file and load into dictionary
# Source: geeksforgeeks.org/load-csv-data-into-list-and-dictionary-using-python/
'''
with open('filehashes.csv', 'r') as data:
	for line in csv.reader(data):
		oldCsvData[line[0]] = [line[1], line[2]]   # add to dictionary
del oldCsvData['File Path']                  # delete CSV header item
del oldCsvData['/']
data.close()                                 # close file
print('Loaded old CSV information...')
'''

# os.walk to iterate 
# Source link: kite.com/python.answers/how-to-list-all-subdirectories-and-files-in-a-given-directory-in-python#
rootDir = '/'
for root, subdirectories, files in os.walk(rootDir):
	for file in files:
		#Source Link: geeksforgeeks.org/python-check-if-string-starts-with-any-element-in-list/
		unhashable = root.startswith(tuple(unhashableLst))
		if unhashable == True:                            # if unhashable directory specified, move to next one
			continue
		else:                                             # if not, save the file name
			fileName = os.path.join(root, file)
			# open file, hash it, and store the file name, the hash, and the time and date
			try:
				f = open(fileName, 'rb')
				bytesToRead = f.read()
				hash = hashlib.sha256(bytesToRead).hexdigest()
				# Source: programiz.com/python-programming/datetime/strftime
				now = datetime.datetime.now()
				timeStamp = now.strftime("%m-%d-%Y %H:%M:%S.%f")
				csvRows[fileName] = [hash, timeStamp]
				f.close()
			except IOError:  # if file can't open (not all files listed in the system actually exist), move on to next file
				continue

print('Traversed through files...')

# List of Added Files
addedFiles = []
# List of deleted files
deletedFiles = []
# List of modified files
modifiedFiles = []
'''
# Compare lists to see modified new files
for key in oldCsvData.keys():
	if key in csvRows:
		if oldCsvData[key][0] == csvRows[key][0]:  # if hashes match
			continue
		else:                                      # if hashes don't match
			modifiedFiles.append(key)          # add to list of modified files
	else:                                              # if the file is a new file
		addedFiles.append(key)                     # add files to the added files list
print('Found modified and added files...')

print('Found deleted files...')
'''

# open the same CSV file and overwrite, adding the contents of csvRows
with open('filehashes.csv', 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	fields = ['File Path', 'Hash', 'Date and Time']
	csvwriter.writerow(fields)
	csvwriter.writerows(csvRows)
print('Wrote new data to CSV file...')
csvfile.close()

'''
# Print changes in files and any new or deleted files 
print('Here is a summary of findings from our search:')
print()

if addedFiles == []:
	print('No new added files')
	print()
else:
	print('Files added to the system:')
	for item in addedFiles:
		print(item)
	print()

if deletedFiles == []:
	print('No new deleted files')
	print()
else:
	print('Files deleted from the system:')
	#for item in deletedFiles:
	#	print(item)
	print()

if modifiedFiles == []:
	print('No new modified files')
	print()
else:
	for item in modifiedFiles:
		print(item)
	print()

'''
