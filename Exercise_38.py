# Create a function that will convert an array containing ASCII codes in a string
def ascii_to_string(array):
    string = ""
    for val in array:
        string = chr(val) + string
    return string


print(ascii_to_string([65, 97, 32, 66, 98]))