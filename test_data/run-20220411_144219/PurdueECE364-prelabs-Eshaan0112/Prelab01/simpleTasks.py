# ######################################################
# Author : Eshaan Minocha
# email : eminocha@purdue.edu
# ID : ee364b01
# Date : 01/16/2022
# ######################################################

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def writePyramids(filePath, baseSize, count, char):                                
    with open(filePath, 'w') as pyramid_file:
        mid = int(baseSize / 2)
        left = mid
        right = mid
        times = count - 1
        for k in range(int(baseSize / 2) + 1):
            for i in range(count):
                for j in range(baseSize):
                    if left <= j <= right:
                        pyramid_file.write(char)
                    else:
                        pyramid_file.write(' ')
                if times:
                    pyramid_file.write(' ')
                    times -= 1
                else:
                    times = count - 1
            left -= 1
            right += 1
            pyramid_file.write('\n')
    return
            
def getStreaks(sequence, letters):
    res = []
    comparison = []
    i = 1
    while i < len(sequence):
        if sequence[i-1] != sequence[i]:
            comparison.append(sequence[0:i])
            sequence = sequence[i:]
            i = 1
        else:
            i += 1
    comparison.append(sequence)
    #print(comparison)
    for i in range(len(comparison)):
        str_val = comparison[i]
        if str_val[0] in letters:
            res.append(str_val)
    return res
    
if __name__ == "__main__":
    writePyramids('TestFile.txt', 13, 6, 'X') # Problem 1

    sequence = "AAASSSSSSAPPPSSPPBBCCCSSS" # Problem 2
    print(getStreaks(sequence, "SAQT"))
    
