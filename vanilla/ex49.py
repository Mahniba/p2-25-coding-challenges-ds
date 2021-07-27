import random
import array

arr = array.array('q', [1, 2, 3, 4, 5, 6])

print("Original array: ", arr)

arr = array.array('q', random.sample(list(arr), 6))

print("Shuffled array: ", arr)