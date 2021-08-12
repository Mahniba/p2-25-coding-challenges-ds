using.system;
class exo32
{
    static void Main()
    {
        string note = "I AM A BOY";
        string caps = CapitalizeFirstLetter(note);
        Console.WriteLine(caps);
    }
    static string CapitalizeFirstLetter(string str)
    {
        str = str.ToLower();
        char[] array = str.ToCharArray();
        if (array.Length >= 1)
        {
            if (char.IsLower(array[0]))
            {
                array[0] = char.ToUpper(array[0]);
            }
        }

        for (int i = 1; i < array.Length; i++)
        {
            if (array[i - 1] == ' ')
            {
                if (char.IsLower(array[i]))
                {
                    array[i] = char.ToUpper(array[i]);
                }
            }
        }

        return new string(array);
    }
}