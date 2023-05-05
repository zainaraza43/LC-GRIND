#include <stack>

class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        char sc;
        
        for (char c: s) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else {
                if (stack.empty()) {
                    return false;
                }
                
                sc = stack.top();
                
                if ((sc == '(' && c == ')') || (sc == '{' && c == '}') || (sc == '[' && c == ']')) {
                    stack.pop();
                    continue;
                } 
                
                return false;
            }
        }
        return stack.empty();
    }
    
};