using System;
using System.Text;

class exo39
{
    static void Main()
    {
        String text = "ATTACKATONCE";
        int s = 4;
        StringBuilder cipher = encrypt(text, s);
        Console.WriteLine(cipher);
    }

    public static StringBuilder encrypt(String text, int s)
    {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < text.Length; i++)
        {
            if (char.IsUpper(text[i]))
            {
                char ch = (char)(((int)text[i] + s - 65) % 26 + 65);
                result.Append(ch);
            }
            else
            {
                char ch = (char)(((int)text[i] + s - 97) % 26 + 97);
                result.Append(ch);
            }
        }
        return result;
    }
}
