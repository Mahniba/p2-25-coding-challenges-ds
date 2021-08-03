arr=[5,10,15,20,25]

max = arr[0]
for i in range(0,len(arr)):
        if arr[i]>max:
            max= arr[i]

print("largest number is:" + str(max))
