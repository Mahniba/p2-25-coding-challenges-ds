def elt_in_arr1(a1, a2):
    return[x for x in a1 if x not in a2]
print(elt_in_arr1([1, 2, 3, 4], [1, 2]))