# This code is meant to go through all the files except specified ones

import os 

rootDir = '/'
for root, subdirectories, files in os.walk(rootDir):
	for subdirectory in subdirectories:
		print(os.path.join(root, subdirectory))
	for file in files:
		print(os.path.join(root, file))
