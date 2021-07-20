n=int(input("find sum of prime numbers n:"))
sum=0
for num in range (2,n+1):
    i=2
    for i in range (2,num):
        if (int(num % i) == 0):
            i = num
            break;
if i is not num:
            sum+=num
print ("\nsum of all prime numbers upto",n,":",sum)