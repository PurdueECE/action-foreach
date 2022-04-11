def getStreakProduct(sequence: str, maxSize: int, product: int) -> list :
	matches = []
	for index_begin in range(len(sequence)) :
		total = 1
		for substring_index in range(len(sequence[index_begin : index_begin + maxSize])) : # substring_index is the index of the number we are calculating at
			#print(f'sequence: \"{sequence[index_begin : index_begin + maxSize]}\"')
			index_end = substring_index + index_begin # the true ending is the index of the original string 'sequence' at the number we are at
			total *= int(sequence[index_end])
			if total == product and substring_index <= maxSize and substring_index + 1 >= 2 :
				matches.append(sequence[index_begin : index_end + 1])
	return matches

def convertToBoolean(num: int, size: int) -> list :
	if type(num) is not int or type(size) is not int :
		return []
	as_binary = bin(num)[2:]
	list_length = size if len(as_binary) < size else len(as_binary)
	list_format = [ True if digit == '1' else False for digit in as_binary ]
	for i in range(list_length - len(list_format)) : # fill extra space with False
		list_format.insert(0, False)
	return list_format

def convertToInteger(boolList: list) -> int :
	if not isinstance(boolList, list) :
		return None
	if not boolList :
		return None
	integer = ""
	for boolean in boolList :
		if not isinstance(boolean, bool) :
			return None
		digit = "1" if boolean is True else "0"
		integer = integer + digit
	return int(integer, 2)

if __name__ == "__main__" :
	print(getStreakProduct("123456789", 3, 6))
	print(getStreakProduct("123456789", 2, 6))
	print(getStreakProduct("123456789", 1, 6))
	print(getStreakProduct("123456789", 3, 504))
	print(getStreakProduct("14822", 3, 32))
	print(convertToBoolean(9, 2))
	print(convertToBoolean("not an int", "also not an int"))
	print(convertToBoolean("not an int", 5))
	print(convertToBoolean(5,            "also not an int"))
	print(convertToInteger(convertToBoolean(5, 8)))
	print(convertToInteger(convertToBoolean(10, 3)))
