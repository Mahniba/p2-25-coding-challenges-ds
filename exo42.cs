using System;


class exo42
{

    public static float radius1;
    public static float radius2;
    private static float dist;

    static void Main(string[] args)
    {
        radius1 = 3.0f;
        radius2 = -2;

        Console.WriteLine(circleIntersect());
    }

    static bool circleIntersect()
    {
        if (dist > (radius1 - radius2) && dist < (radius1 + radius2))
        {
            return true;
        }

        return false;
    }
}