using System;

class exo41
{
    public static double x1;
    public static double y1;
    public static double x2;
    public static double y2;

    static void Main(string[] args)
    {
        x1 = -3; y1 = 0; x2 = 5; y2 = 2;

        Console.WriteLine(distance2Points() + " units");
    }

    public static double distance2Points()
    {
        double distance1 = Math.Pow((x2 - x1), 2);
        double distance2 = Math.Pow((x2 - x1), 2);

        return Math.Sqrt(distance1 + distance2);

    }
}