class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> mapping;

        for (char c : s) {
            mapping[c]++;
        }

        for (char c: t) {
            mapping[c]--;
        }

        for(auto const& [key, val]: mapping) {
            if (val != 0) return false;
        }
        return true;
    }
};