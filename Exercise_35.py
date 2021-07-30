import csv

with open("filename.csv", newline='') as csvfile:
    data = list(csv.reader(csvfile))
    print(data)