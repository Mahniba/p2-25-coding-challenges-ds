def longestWord(string):
    list = string.split()
    long = 0;
    for elt in list:
        if len(elt) > long:
            long = len(elt)
            result = elt
    return result
print(longestWord("Girl meets the world"))
