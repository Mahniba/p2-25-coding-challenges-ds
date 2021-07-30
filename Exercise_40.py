# Implement the bubble sort algorithm for an array of numbers
def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

print(bubbleSort([6,4,1,3,4,0,4]))