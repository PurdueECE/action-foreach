# ######################################################
# Author : Xingjian Wang
# email : wang5066@purdue.edu
# ID: ee364b03
# Date : Jan 19, 2022
# ######################################################

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def evenResult(number_list, string):
    # Decide which command is given
    result = 0
    if (string == "sum"):
        for element in number_list:
            # Error handling
            try:
                is_odd = element % 2
            except TypeError as err:
                print("number_list should be list")
                # Since the whole type is incorrect,
                # no need to check further element
                break
            except ValueError as err:
                # Further element may be of correct type,
                # so does not break
                print("element in number_list should be int")
            else:
                if not is_odd:
                    result += element
            finally:
                pass
    elif (string == "product"):
        result = 1  # the base for product is 1
        for element in number_list:
            if element % 2 == 0:
                result *= element
    return result


# Self-testing block
# ######################################################
# array = [3,5,2,4,1,6]
# print(evenResult(array, "sum"))
# print(evenResult(array, "product"))
