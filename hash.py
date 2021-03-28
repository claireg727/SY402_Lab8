# This code is meant to go through all the files except specified ones

import os
import hashlib 
import csv
import datetime

unhashableLst = [
	'/dev',
	'/proc',
	'/run',
	'/sys',
	'/tmp',
	'/var/lib',
	'/var/run'
]

csvRows = []

# os.walk to iterate 
# Source link: kite.com/python.answers/how-to-list-all-subdirectories-and-files-in-a-given-directory-in-python#
rootDir = '/'
for root, subdirectories, files in os.walk(rootDir):
	for file in files:
		#Source Link: geeksforgeeks.org/python-check-if-string-starts-with-any-element-in-list/
		unhashable = root.startswith(tuple(unhashableLst))
		if unhashable == True:
			continue
		else:
			fileName = os.path.join(root, file)
			try:
				f = open(fileName, 'rb')
				bytesToRead = f.read()
				hash = hashlib.sha256(bytesToRead).hexdigest()
				# Source: programiz.com/python-programming/datetime/strftime
				now = datetime.datetime.now()
				timeStamp = now.strftime("%m-%d-%Y %H:%M:%S.%f")
				row = [fileName, hash, timeStamp]
				csvRows.append(row)
				f.close()
			except IOError:
				continue

with open('filehashes.csv', 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	fields = ['File Path', 'Hash', 'Date and Time']
	csvwriter.writerow(fields)
	csvwriter.writerows(csvRows)

csvfile.close()
