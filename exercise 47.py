import copy
x = [[24,23,25],[32,43,54]]
y = copy.deepcopy(x)
print(y)
y[0][2] = 100
print(y)
print(x)