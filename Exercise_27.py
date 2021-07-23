# Create a function that will receive an array of numbers as argument and will return a
# new array with distinct elements
import random
def array_of_distinct_elements(array):
    result = []
    for i in range(len(array)):
        while len(result) != len(array):
            elt = random.randint(min(array), max(array)*2)
            if elt in array or elt in result:
                continue
            result.append(elt)
    return result

print(array_of_distinct_elements([1,2,3,4,5]))

