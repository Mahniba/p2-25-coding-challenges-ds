import random
import array as arr
def unique_numbers(m):
    array = arr.array("i",[])
    li = range(0,m)
    li = random.sample(li,m)
    for items in li:
        array.append(items)
    return array


value = unique_numbers(16)
print(value )