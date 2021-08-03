
def distinct(array):
    result = []
    for elt in array:
        if elt not in result:
            result.append(elt)
    return result
print(distinct([1,2,2,3,4,5]))