# This code is meant to go through all the files except specified ones

import os               # used for the os.walk() function
import hashlib          # used to hash the files
import csv              # used to create and write to a CSV file 
import datetime         # used to obtain the current time and date

# import old CSV file and store in dictionary
# Source: geeksforgeeks.org/load-csv-data-into-list-and-dictionary-using-python/
oldCsvData = {}

with open('filehashes.csv', 'r') as data:
	for line in csv.reader(data):
		oldCsvData[line[0]] = [line[1], line[2]]
del oldCsvData['File Path']
data.close()

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
csvRows =[]
csvRowsDict = {}

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
				row = [fileName, hash, timeStamp]
				csvRows.append(row)
				csvRowsDict[fileName] = [hash, timeStamp]
				f.close()
			except IOError:  # if file can't open (not all files listed in the system actually exist), move on to next file
				continue

# compare dictionaries to find differences
addedFiles = []
modifiedFiles = []
 
for key in csvRowsDict.keys():
	if key in oldCsvData.keys():
		if oldCsvData[key][0] == csvRowsDict[key][0]:
			continue
		else:
			modifiedFiles.append(key)
	else:
		addedFiles.append(key)


deletedFiles = []

for key in oldCsvData.keys():
	if key not in csvRowsDict.keys():
		deletedFiles.append(key)



# open the output CSV file and add the contents of csvRows
with open('filehashes.csv', 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	fields = ['File Path', 'Hash', 'Date and Time']
	csvwriter.writerow(fields)
	csvwriter.writerows(csvRows)

csvfile.close()

# Print out differences in files 
print("Summary of findings:")
print()
if addedFiles == []:
	print('No added files')
else:
	print("These files were added:")
	for item in addedFiles:
		print(item)
print()
if modifiedFiles == []:
	print('No modified files')
else:	
	print("These files were modified:")
	for item in modifiedFiles:
		print(item)

print()
if deletedFiles == []:
	print('No deleted files')
else:
	print('These files were deleted:')
	for item in deletedFiles:
		print(item)
