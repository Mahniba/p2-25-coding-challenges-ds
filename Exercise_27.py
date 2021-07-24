# Create a function that will receive an array of numbers as argument and will return a
# new array with distinct elements
def array_of_distinct_elements(array):
    result = []
    for elt in array:
        if elt not in result:
            result.append(elt)
    return result


print(array_of_distinct_elements([1,2,1,4,3,4,5]))


