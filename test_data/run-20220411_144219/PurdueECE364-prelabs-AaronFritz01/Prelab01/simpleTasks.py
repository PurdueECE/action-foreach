# ######################################################
# Author : Aaron Fritz
# email : fritzam@purdue.edu
# ID : ee364b20
# Date : 1/30/22
# ######################################################


# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def getStreaks(sequence: str, streakChars: str):
    streakCharList = list(streakChars)
    sequence = list(sequence + "_")
    finalList = []
    currentStreak = []
    streakCount = 0
    previousSequenceChar = sequence[0]
    for sequenceChar in sequence:
        if (previousSequenceChar != sequenceChar) & (currentStreak != []):
            finalList.append(''.join(currentStreak))
            currentStreak = []
        if (sequenceChar in streakCharList):
            streakCount+=1
        if (streakCount != 0):
            currentStreak.append(sequenceChar)
            streakCount = 0
            previousSequenceChar = sequenceChar
    return finalList

def writePyramids(filePath: str, baseSize, count, char):
    with open(filePath, 'w') as file: 
        for i in range (baseSize, -1, -1):
            string = " " * i + char * (baseSize - 2*i) + " " * (i+1)
            file.write(string*count)
    return 0

