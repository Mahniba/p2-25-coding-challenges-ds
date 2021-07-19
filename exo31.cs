using System;

class exo31
{
    static int OUT = 0;
    static int IN = 1;

    static void Main(string[] args)
    {
        string note = "One two        five\nsix\t";
        Console.WriteLine(countWords(note));
    }

    static int countWords(string str)
    {
        int state = OUT;
        int wc = 0;
        int i = 0;

        while (i < str.Length)
        {
            if (str[i] == ' ' || str[i] == '\n' || str[i] == '\t')
            {
                state = OUT;
            }

            else if (state == OUT)
            {
                state = IN;
                wc++;
            }
            i++;
        }

        return wc;
    }
}