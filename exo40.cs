using System;

class exo40
{
    static void Main(string[] args)
    {
        long[] array = { 8, 6, 9, -5, -7, -6, 12, 15, 10, 1, 20, 4, -3, 2 };
        long num = array.LongLength;
        bubbleSort(array, num);
        for (long c = 0; c < num; c++)
        {
            Console.WriteLine(array[c]);
        }
    }

    static void bubbleSort(long[] list, long n)
    {
        long t;

        for (long c = 0; c < (n - 1); c++)
        {
            for (long d = 0; d < n - c - 1; d++)
            {
                if (list[d] > list[d + 1])
                {
                    t = list[d];
                    list[d] = list[d + 1];
                    list[d + 1] = t;
                }
            }
        }
    }
}