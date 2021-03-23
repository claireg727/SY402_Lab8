# This code is meant to go through all the files except specified ones

import os 

unhashableLst = [
	'/dev',
	'/proc',
	'/run',
	'/sys',
	'/tmp',
	'/var/lib',
	'/var/run'
]

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
			print(os.path.join(root, file))
