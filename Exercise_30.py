# Create a function that will add two positive numbers of indefinite size. The numbers
# are received as strings and the result should be also provided as string.
def add(num1, num2):
    result = ""
    carry = 0
    if len(num1) > len(num2):
        num2 = "0"*(len(num1) - len(num2)) + num2
    else:
        num1 = "0"*(len(num2)-len(num1)) + num1
    for i in range(1, (max(len(num1), len(num2)))+1):
        result = str(((int(num1[-i]) + int(num2[-i])) + carry) % 10) + result
        carry = (int(num1[-i]) + int(num2[-i]) + carry) // 10
    if carry == 0:
        return result
    else:
        return str(carry) + result


print(add("9913", "239"))
