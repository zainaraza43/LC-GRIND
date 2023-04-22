// 1st submission, basically brute forced :(

#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<int, int> m;
        for (char c : s)
            m[c] += 1;
        for (char c : t)
            m[c] -= 1;
        for (pair<int, int> p : m)
        {
            if (p.second != 0)
                return false;
        }
        return true;
    }
};

// reworked to beat 97.5% :)

#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        int a[26] = {0};
        int size = s.size();
        if (size != t.size())
            return false;
        for (int i = 0; i < size; ++i)
        {
            a[s[i] - 'a'] += 1;
            a[t[i] - 'a'] -= 1;
        }
        for (int i = 0; i < 26; ++i)
            if (a[i] != 0)
                return false;
        return true;
    }
};