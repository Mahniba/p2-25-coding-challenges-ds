def sum_jarray(array):
    max = 0
    for i in range(len(array)):
        if type(array[i]) == int:
            max += array[i]
        else:
            for items in array[i]:
                max += items
    return max
value = sum_jarray([])
print(value)