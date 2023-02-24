import array as arr
def string_ASCII(text):
    n = 0
    text = arr.array(text)
    for i in text:
        text(n) = ord(i)
        n += 1
    return text

letter = input("i love food")
print(string_ASCII(letter))