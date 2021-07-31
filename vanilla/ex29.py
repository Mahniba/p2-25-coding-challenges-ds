def isPrime(y):
    flag = False
    if y == 1:
        flag = False

    for i in range(2,y):
        if y % i == 0:
           flag = False
        else:
            flag = True
        return flag
y=int(input("enter a number: "))
print(isPrime(y))

def distance(n):
    last_prime = 2
    i = last_prime + 1
    counter = 1
    while counter < n:
        if isPrime(i):
            print(f"{i - last_prime} \t {i} - {last_prime} ")
            last_prime = i
            counter += 1
        i += 1


distance(100)