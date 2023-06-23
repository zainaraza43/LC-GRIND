/**
 * Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
 * 
 * In other words, return true if one of s1's permutations is the substring of s2.
 * 
 * 
 * Example 1:
 *
 * Input: s1 = "ab", s2 = "eidbaooo"
 * Output: true
 * Explanation: s2 contains one permutation of s1 ("ba").
 *
 * Example 2:
 *
 * Input: s1 = "ab", s2 = "eidboaoo"
 * Output: false
 *  
 * Constraints:
 * - 1 <= s1.length, s2.length <= 104
 * - s1 and s2 consist of lowercase English letters.
 */

bool equal(uint8_t *h1, uint8_t *h2) {
    for (int i = 0; i < 26; ++i) if (h1[i] != h2[i]) return false;
    return true;
}

bool checkInclusion(char * s1, char * s2){
    int l1 = strlen(s1), l2 = strlen(s2);
    if (l1 > l2) return false;
    uint8_t hist1[26] = {0}, hist2[26] = {0};
    uint hash1 = 0, hash2 = 0;
    for (int i = 0; i < l1; ++i) {
        ++hist1[s1[i] - 'a'];
        ++hist2[s2[i] - 'a'];
        hash1 += s1[i];
        hash2 += s2[i];
    }
    for (int i = 0; i < l2 - l1; ++i) {
        if (hash1 == hash2 && equal(hist1, hist2)) return true;
        ++hist2[s2[i + l1] - 'a'];
        --hist2[s2[i] - 'a'];
        hash2 += s2[i + l1];
        hash2 -= s2[i];
    }
    if (hash1 == hash2 && equal(hist1, hist2)) return true;
    return false;
}
