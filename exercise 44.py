from math import pow
def convert(text):
    l = len(text)
    sum = 0
    for num in text:
        sum += int(num)*pow(2, l-1)
        l -= 1
    return round(sum)

print(convert("1101"))