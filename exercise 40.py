def  bubble_sort(t: object, size: object) -> object:
     for i in range(0,len(size)):
        for j in range(0,len(size)):
         if(t[j]>t[j+1]):
             temp= t[j]
             t[j]=t[j+1]
             t[j+1]=temp


element=int(input("enter the elements of the array: "))
value=int(input("enter the size of the array"))
print(bubble_sort(element,value))