#######################################################
# Author: Deyuan Sun
# email: sun829@purdue.edu
# ID: ecea04
# Date: 1/13/2022
#######################################################
import re
#######################################################
# No Module -Level Variables or Statements!
# ONLY FUNCTIONS BEYOND THIS POINT!
#######################################################
def writePyramids(filePath, baseSize, count, char):
	f = open(filePath, "w+")
	b = int ((baseSize+1)/2)
	for i in range(0,b): # outter layer
		tempStr = char
		for a in range(0,i):
			tempStr = char + tempStr + char
		rtStr = ""
		for j in range(len(tempStr), baseSize, 2):
			tempStr = " "+tempStr+" "
		for k in range(0, count):
			rtStr += tempStr 
			if k != (count - 1):
				rtStr += " " 
		rtStr += "\n"
		f.writelines(rtStr)
	f.close()

def getStreaks(sequence, letters):
	rtList = []
	for i in letters:
		result = re.findall(i+"*", sequence)
		rtList += result
	while '' in rtList:
		rtList.remove('')
	return rtList


# This block is optional and can be used for testing.
# We will NOT look into its content.
#######################################################
if __name__ == "__main__":
# Write anything here to test your code.
	#writePyramids('trypyramid13.txt', 13, 6, 'X')
	sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
	print(getStreaks(sequence, "SAQT"))