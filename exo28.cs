using System;

class exo28
{
	static void Main(string[] args)
    {
        int[] array = new int[100];
        int num = array.Length;

        int sum = sumOfPrime(num);

        Console.Write(sum);
    }

    static int sumOfPrime(int n)
    {
        int sum = 0;
        for (int i = 2; i < n; i++)
        {
            if (isPrime(i))
            {
                sum += i;
            }
        }
        return sum;
    }

    static bool isPrime(int n)
    {
        for (int i = 2; i < n; i++)
        {
            if (n % i == 0)
            {
                return false;
            }
        }
        return true;
    }
}