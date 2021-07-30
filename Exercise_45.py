# Create a function to calculate the sum of
# all the numbers in a jagged array (array contains numbers or other
# arrays of numbers on an unlimited number of levels)
import array
def sum_of_jagged_array(array):
    result = 0
    for elt in array:
        if elt in array:
            if isinstance(elt, list):
                result += sum(elt)
            else:
                result += elt
    return result


print(sum_of_jagged_array([2, [1,2,0], 3, 2]))