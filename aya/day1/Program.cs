class TestClass
{
    static void Main(string[] args)
    {
        int[] array1 = new int[] { 1, 2, 3, 4, 5, 1, 6, 2 };
        int[] array2 = new int[] { 1, 2, 3, 4, 5, 6, 7 };

        Console.WriteLine(Duplicates.has_duplicates(array1));
        Console.WriteLine(Duplicates.has_duplicates(array2));

    }
}