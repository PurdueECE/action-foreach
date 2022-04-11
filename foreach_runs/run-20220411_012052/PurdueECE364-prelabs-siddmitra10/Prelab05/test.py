from pprint import pprint as pp
# Create a large dictionary:
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
occurrences = [32, 12, 67, 21, 9, 45, 83]
dict_example = {day: occurrence for day, occurrence in zip(days, occurrences)}
# Regular Printing
print(dict_example)
# Pretty Printing
pp(dict_example)