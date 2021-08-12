using System;

class exo27
{
    static void Main(string[] args)
    {
        int[] myarray = { 5, 2, -4, 6, 9, 2, 8, 5, 2, 7, 1, 5, 8 };
        int n = myarray.Length;
        distinctElements(myarray, n);
    }

    static void distinctElements(int[] myarray1, int n)
    {
        int j;
        for (int i = 0; i < n; i++)
        {
            for (j = 0; j < i; j++)
            {
                if (myarray1[i] == myarray1[j])
                {
                    break;

                }
            }
            if (i == j)
            {
                Console.Write("{0}  ", myarray1[i]);
            }
        }
    }
}