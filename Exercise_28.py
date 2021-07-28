
# Calculate the sum of the first 100 prime numbers
from Exercise_16 import is_prime
def sum_of_first_n_prime_numbers(n):
    sum = 0
    i = 1
    counter = 0
    array = []
    while counter < n:
        if is_prime(i):
            array.append(i)
            sum += i
            counter += 1
        i += 1
    return sum, array


print(f"Sum of first 100 prime numbers is {sum_of_first_n_prime_numbers(100)}")
