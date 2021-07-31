import csv

with open("filename.csv", newline='') as csvfile:
    output = list(csv.reader(csvfile))
    print(output)