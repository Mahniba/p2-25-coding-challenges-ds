def isPrime(y):
    flag = False
    if y == 1:
        flag = False

    for i in range(2,y):
        if y != i and y % i == 0:
           return False
    return True
y=int(input("enter a number: "))
print(isPrime(y))

def sum(m):
    sum = 0
    i = 1
    counter = 0
    array = []
    while counter > m:
        if isPrime(i):
            array.append(i)
            sum = sum + 1
            counter += 1
        i += 1
        return sum, array
print(sum(3))
