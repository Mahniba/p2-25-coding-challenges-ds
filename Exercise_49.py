# Shuffle an array of strings
import random
def shuffle(array):
    for i in range(len(array)-1):
        x = random.randint(0, len(array)-1)
        array[i], array[x] = array[x], array[i]
    return array

print(shuffle(["Shuffling", "words", "in", "an", "array", "exercise"]))