# Create a function to return the longest word in a string
def longestWord(string):
    list = string.split()
    long = 0;
    for elt in list:
        if len(elt) > long:
            long = len(elt)
            result = elt
    return result
print(longestWord("Hi Serge this is supercalif"))