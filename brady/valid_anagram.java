class Solution {
    // O(max(m,n)) time, O(max(m,n)) space, where m and n are the lengths of s and t respectively
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) return false;

        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();

        for (int i = 0; i < s.length(); ++i) {
            char cs = s.charAt(i);
            char ct = t.charAt(i);
            sMap.merge(cs, 1, Integer::sum);
            tMap.merge(ct, 1, Integer::sum);
        }

        if (sMap.size() != tMap.size()) return false;

        for (Map.Entry<Character, Integer> sEntry : sMap.entrySet()) {
            int sCount = sEntry.getValue();
            int tCount = tMap.getOrDefault(sEntry.getKey(), 0); // no counts will be 0 in the map so the next line returns
            if (sCount != tCount) return false;
        }

        return true;
    }
}
