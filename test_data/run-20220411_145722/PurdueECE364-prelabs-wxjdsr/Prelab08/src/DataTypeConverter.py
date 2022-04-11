# ######################################################
# Author :  Xingjian Wang
# email :   wang5066@purdue.edu
# ID:       ee364b03
# Date :    Mar 6, 2022
# ######################################################
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
def getStreakProduct(sequence, maxSize, product):
    target_list = []
    sequence_list = [int(x) for x in sequence]
    list_len = len(sequence_list)
    # Calculate the product
    for start_index in range(0, list_len):
        current_product = 1
        current_index = start_index
        current_size = 0
        while (current_product < product and current_index < list_len
                and current_size < maxSize):
            current_product *= sequence_list[current_index]
            current_index += 1
            current_size += 1
        # Return to the normal position after the last loop
        current_index -= 1
        # Check if it does not reach the product
        if current_product != product:
            continue
        # Add the matched substring into list
        target_list.append(sequence[start_index: current_index + 1])
        # Check if there is 1 after (this still reaches the product)
        while (current_index < list_len
                and sequence_list[current_index + 1] == 1):
            # this involves the extra "1"
            target_list.append(sequence[start_index: current_index + 2])
            current_index += 1
    return target_list


def convertToBoolean(num, size):
    # If @num is not integer, return an empty list
    if not isinstance(num, int):
        return list()
    # Convert @num into binary format using format()
    num_binary = format(num, f'0{size}b')
    boolean_list = [True if item == '1' else False for item in num_binary]
    return boolean_list


def convertToInteger(boolList):
    # Check the input type
    if not isinstance(boolList, list):
        return None
    if len(boolList) == 0:
        return None
    for element in boolList:
        if not isinstance(element, bool):
            return None
    # Conversion
    int_list = ['1' if element else '0' for element in boolList]
    value = int("".join(int_list), 2)
    return value
