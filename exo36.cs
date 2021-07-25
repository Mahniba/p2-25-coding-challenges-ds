using System;

class exo36
{
    static void Main()
    {
        string note = "Kanyelings";
        StringToArray(note);
    }

    static void StringToArray(string str)
    {
        char[] array = new char[str.Length];
        for (int i = 0; i < array.Length; i++)
        {
            array[i] = str[i];
        }

        foreach (char ch in array)
        {
            Console.WriteLine(ch);
        }

    }
}