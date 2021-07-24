# Create a function that will add two positive numbers of indefinite size. The numbers
# are received as strings and the result should be also provided as string.
def add(num1, num2):
    result = ""
    carry = 0
    if len(num1) > len(num2):
        longest = num1
    else:
        longest = num2
    for i in range(1, (max(len(num1), len(num2)))+1):
        try:
            result = str(((int(num1[-i]) + int(num2[-i])) + carry) % 10) + result
            carry = (int(num1[-i]) + int(num2[-i]) + carry) // 10
        except IndexError:
            result = str(((int(longest[-i])) + carry) % 10) + result
            carry = ((int(longest[-i])) + carry) // 10
    if carry == 0:
        return result
    else:
        return str(carry) + result


print(add("9913", "239"))
