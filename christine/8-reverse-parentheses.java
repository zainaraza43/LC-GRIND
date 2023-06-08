import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> brackets = new Stack<>();
        int len = s.length();
        for(int i = 0; i < len; i++){
            switch(s.charAt(i)){
                case '(':
                    brackets.push(')');
                    break;
                case '{':
                    brackets.push('}');
                    break;
                case '[':
                    brackets.push(']');
                    break;
                default:
                    if (brackets.empty() || s.charAt(i) != brackets.pop()){
                        return false;
                    }
            }
        }

        return brackets.empty();
    }
}