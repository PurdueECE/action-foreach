def convertToBoolean(num,size):
    # num = decimal number
    # size = number of list elements
    if isinstance(num,int) != True :
        return []
    if isinstance(size,int) != True:
        return []
    result = [int(i) for i in list('{0:0b}'.format(num))]
    min_length = size - len(result) # number of zeros we need to add
    # adding zeros to list
    if len(result) < size:
        for i in range(min_length):
            result.insert(0,0)
    # turn into strings
    str_result = list(map(str, result)) 

    new_results = []
    for i in str_result:
        new_result = i.replace('0','False')
        new_results.append(new_result)

    new_results2 = []
    for i in new_results:    
        new_result2 = i.replace('1','True')
        new_results2.append(new_result2)

    return new_results2

if __name__ == '__main__':
    z = convertToBoolean(8,5)
    print(z)