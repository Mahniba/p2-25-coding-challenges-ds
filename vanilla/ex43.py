def unidimensional(array, num):
    return[row[num] for row in array]

print(unidimensional([[2,3,7], [3,8,9], [2,1,0]], 2))