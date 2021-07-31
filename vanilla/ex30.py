def add(num1, num2):
    result = ""
    carry = 0
    if len(num2) < len(num1):
        longest = num1
        num2 = "0"*(len(num1) - len(num2)) + num2
    else:
        longest = num2
        num1 = "0"*(len(num2)-len(num1)) + num1
    for i in range(1, (max(len(num1), len(num2)))+1):
        try:
            result = str(((int(num1[-i]) + int(num2[-i])) + carry) % 10) + result
            carry = (int(num1[-i]) + int(num2[-i]) + carry) // 10
        except IndexError:
            result = str(((int(longest[-i])) + carry) % 10) + result
            carry = ((int(longest[-i])) + carry) // 10
        result = str(((int(num1[-i]) + int(num2[-i])) + carry) % 10) + result
        carry = (int(num1[-i]) + int(num2[-i]) + carry) // 10
    if carry == 0:
        return result
    else:
        return str(carry) + result

print(add("9913", "239"))