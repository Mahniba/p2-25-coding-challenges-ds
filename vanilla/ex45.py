import array
def sumOfJaggedArray(array):
    result = 0
    for elt in array:
        if elt in array:
            if isinstance(elt, list):
                result += sum(elt)
            else:
                result += elt
    return result


print(sumOfJaggedArray([5, [1, 6, 3], 4, 7]))