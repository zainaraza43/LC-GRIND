namespace Anagram
{
    public class checkAnagram
    {
        public static bool isAnagram(string s, string t)
        {
            var s1 = string.Concat(s.OrderByDescending(c => c));
            var t1 = string.Concat(t.OrderByDescending(c => c));
            if (string.Compare(s1, t1) == 0)
            {
                return true;
            }
            return false;
        }
    }
}
