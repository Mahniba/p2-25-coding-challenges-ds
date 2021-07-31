# Create a function that will receive a bi-dimensional array as argument and a
# number and will extract as a unidimensional array the column specified by the
# number

def unidimensional(array, num):
    return[row[num] for row in array]

print(unidimensional([[2,3,7], [3,8,9], [2,1,0]], 2))
