s = "Hello world welcome"
word = ''
maxLen = 0
maxWord = ''
for c in s+' ':
    if c == ' ':
        if len(word) > maxLen:
            maxWord = word
        word = ''
    else:
        word += c


print("Longest word:", maxWord)
print("Length:", len(maxWord))