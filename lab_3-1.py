# Author: JD 03/07/2022

def r_max(nested_num_lst): 
    # Mark the current number
    current = 0
    for element in nested_num_lst:
        if type(element) == list:
            current = r_max(element) 
        # If the current working number is greater than the recorded number, then the variable "current" will be replaced
        elif element > current:
            current = element
    return current

print(r_max([0,1,2,3,4,[7,6]]))