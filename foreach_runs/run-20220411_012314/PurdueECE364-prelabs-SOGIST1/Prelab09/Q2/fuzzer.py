import random
# fuzzer for bool_to_int
def fuzzer(max_length:int = 100) -> list :
	random_output = []
	for index in range(max_length) :
		random_bool = True if random.randrange(0, 2) == 1 else False
		random_output.append(random_bool)
	 
	return random_output

if __name__ == "__main__" :
	print(fuzzer(3))
	print(fuzzer(5))
	print(fuzzer() )
