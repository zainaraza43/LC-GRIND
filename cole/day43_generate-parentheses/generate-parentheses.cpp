// the proper solution in C++ because I have an interview in this language tomorrow

class Solution {
public:
    vector<string> recurse(string s, int left, int right, int n) {
        if (s.length() == n * 2) {
            return {s};
        }
        vector<string> v;
        if (left < n) {
            vector<string> l = recurse(s + '(', left + 1, right, n);
            v.insert(
                v.end(),
                std::make_move_iterator(l.begin()),
                std::make_move_iterator(l.end())
            );
        }

        if (right < left) {
            vector<string> l = recurse(s + ')', left, right + 1, n);
            v.insert(
                v.end(),
                std::make_move_iterator(l.begin()),
                std::make_move_iterator(l.end())
            );
        }
        return v;
    }
    vector<string> generateParenthesis(int n) {
        return recurse("", 0, 0, n);
    }
};