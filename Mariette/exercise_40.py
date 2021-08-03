def bubblesort(arr):


    for i in range (len(arr)-1):
        for j in range (0,len(arr)-i-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

print(bubblesort(arr = [76,78,34,21,22,19]))
