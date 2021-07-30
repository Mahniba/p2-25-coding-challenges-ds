# Create a function that will convert a string in an array containing the ASCII codes of
# each character
def array_of_ascii(string):
    return [ord(char) for char in string]

print(array_of_ascii("aA bcdefg"))