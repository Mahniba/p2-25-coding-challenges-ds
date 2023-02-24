import csv
def csv(text):
    values = []
    n = 0
    text = text. split(",")
    for i in text:
        values.insert(n,list(i))
        n += 1
    return values

print(csv("me,myself,i"))