import java.util.HashMap;
import java.util.Map.Entry;

class Solution {
    public boolean isAnagram(String s, String t) {
        int slen = s.length();
        int tlen = t.length();
        HashMap<Character, Integer> schar = new HashMap<Character, Integer>();
        int frequency;

        for(int i = 0; i < slen; i++){
            frequency = schar.get(s.charAt(i)) == null ? 0 : schar.get(s.charAt(i));
            schar.put(s.charAt(i), frequency + 1); //find the frequency of the characters
        }

        for(int i = 0; i < tlen; i++){
            frequency = schar.get(t.charAt(i)) == null ? 0 : schar.get(t.charAt(i));
            schar.put(t.charAt(i), frequency - 1); //check if the frequency matches
        }

        for (Entry<Character, Integer> e : schar.entrySet()) {
            if (e.getValue() != 0){
                return false;
            }
        }

        return true;
    }
}