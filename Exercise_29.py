
# Print the distance between the first 100 prime numbers
def is_prime(number):
    if number <= 1:
        result = False
    elif number == 2:
        result = True
    for i in range(2, number):
        if number % i == 0:
            result = False
            break
        result = True
    return result


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
