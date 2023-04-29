/* Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.
*/
public class Duplicates
{
    public static bool has_duplicates(int[] array)
    {
        for (int i = 0; i < array.Length; i++)
        {
            for (int j = i + 1; j < array.Length; j++)
            {
                if (array[i] == array[j])
                {
                    return true;
                }
            }
        }
        return false;
    }

}