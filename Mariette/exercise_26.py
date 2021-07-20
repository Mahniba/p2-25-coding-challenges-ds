arr1=[1,2,3,4,5]
arr2=[1,2,4,6,8,10]
k=len(arr1)
m=len(arr2)
def findMissing(arr1,ar2,k,m):
    for i in range (k):
        for j in range (m):
            if (arr1[i]==arr2[j]):
                break
        if (j == m-1):
            print(arr1[i],end=" ")
    findMissing(arr1,arr2,k,m)

