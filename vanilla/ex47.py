import copy
def deepCopy(array):
    return [copy.deepcopy(array)]
print(deepCopy([2, 3,4]))