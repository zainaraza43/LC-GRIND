class Solution {
  
    // O(n) time, O(n) space
    public boolean isValid(String s) {

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); ++i) {
            switch (s.charAt(i)) {
                case '(':
                case '{':
                case '[':
                    stack.push(s.charAt(i));
                    break;
                case ')':
                    if (stack.isEmpty() || stack.pop() != '(') return false;
                    break;
                case '}':
                    if (stack.isEmpty() || stack.pop() != '{') return false;
                    break;
                case ']':
                    if (stack.isEmpty() || stack.pop() != '[') return false;
            }
        }

        return stack.isEmpty();
    }
}
