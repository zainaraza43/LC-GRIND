import java.util.Arrays;

class Solution {
    public boolean isAnagram(String s, String t) {
        int slen = s.length();
        int tlen = t.length();
        int[] freqDiff = new int[26];
        int[] eqFreq = new int[26]; //java inits array to 0

        if (slen == tlen){//only works when slen = tlen, so no missing characters to check
            for(int i = 0; i < slen; i++){
                //if the frequency of the character is equal, then the element at the index is 0
                freqDiff[s.charAt(i) - 'a']++; //s and t are lowercased strings
                freqDiff[t.charAt(i) - 'a']--;
            }

            return Arrays.equals(freqDiff, eqFreq);
        }
        
        return false;
    }
}