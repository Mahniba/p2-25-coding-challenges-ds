import random
def shuffle(array):
    for i in range(len(array)-1):
        x = random.randint(0, len(array)-1)
        array[i], array[x] = array[x], array[i]
    return array

print(shuffle(["I", "am ", "facing", "difficulties", "with", "this", "exercises"]))