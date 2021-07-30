# Create a function that will convert a string
# containing a binary number into a number
def binary_to_number(str):
    result = 0
    for i in range(len(str)):
        if int(str[i]) != 0 and int(str[i]) != 1:
            return "Please enter a string containing binary numbers only"
        elif int(str[i]) == 1:
            result += 2**(len(str) - i - 1)
        else:
            result += 0
    return result

