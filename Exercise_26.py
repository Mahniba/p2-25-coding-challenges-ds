# Create a function that will receive two arrays and will return an array with
# elements that are in the first array but not in the second
def elements_in_first_array_only(arr1, arr2):
    result = []
    for elt in arr1:
        if elt not in arr2:
            result.append(elt)
    return result

print(elements_in_first_array_only([1,4,5,3], [1,5,7,9,0]))