def distance_between_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    for i in range(2,number):
        if number%i == 0:
            return False
    return True

value = input(100)
print(distance_between_prime(value))