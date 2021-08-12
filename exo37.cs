using System;

class exo37
{
    static void Main(string[] args)
    {
        string str = "7597110121101108105110103115";
        int len = str.Length;
        asciiToSen(str, len);
        Console.WriteLine();
    }

    static void asciiToSen(String str, int len)
    {
        int num = 0;
        for (int i = 0; i < len; i++)
        {
            num = num * 10 + (str[i] - '0');

            if (num >= 32 && num <= 122)
            {
                char ch = (char)num;
                Console.Write(ch);
                num = 0;
            }
        }
    }
}