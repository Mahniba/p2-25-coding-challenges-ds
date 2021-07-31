def sumOfNumbers(string):
    list = string.split(',')
    sum = 0
    for num in list:
        sum =sum + float(num)
    return sum

print(sumOfNumbers("1,2,3"))