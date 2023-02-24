//Challenge 28 is to Calculate the sum of first 100 prime numbers

#include<iostream> 
using namespace std; 
 
int main() 
{ 
	int n=100, isprime = 1, count, i, num=3,sum=2; 
 	 
	if(n>=1) 
	{ 
		for (count=2; count<=n ; ) 
		{ 
			for(i=2; i<=num-1; i++) 
			{ 
				if(num%i==0) 
				{ 
					isprime = 0; 
					break; 
				} 
			} 
	 
			if(isprime) 
			{ 
				sum += num; 
				count++; 
			} 
	 
		isprime = 1; 
		num++;   	 
		} 
	} 
	 
	cout<<"The sum of first "<<n<<" prime numbers is "<<sum;		 
} 
