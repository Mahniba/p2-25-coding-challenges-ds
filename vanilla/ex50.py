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