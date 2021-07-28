
# Print the distance between the first 100 prime numbers
from Exercise_16 import is_prime

def distance_between_prime(n):
    last_prime = 2
    i = last_prime + 1
    counter = 1
    while counter < n:
        if is_prime(i):
            print(f"{i - last_prime} \t {i} - {last_prime} ")
            last_prime = i
            counter += 1
        i += 1


distance_between_prime(100)
