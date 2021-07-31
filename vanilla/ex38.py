def ASCIIToString(array):
    string = ""
    for val in array:
        string = chr(val) + string
    return string


print(ASCIIToString([85, 63, 20, 50]))