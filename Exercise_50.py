# Create a function that will receive n as argument and return an array of n
# random numbers from 1 to n. The numbers should be unique inside the array.
import random
def array_of_random_numbers(n):
    result = []
    count = 0
    while count < n:
        x = random.randint(1, n)
        if x not in result:
            result.append(x)
            count += 1
    return result
print(array_of_random_numbers(10))