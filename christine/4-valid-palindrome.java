import java.util.Stack;

class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        Stack<Character> stack = new Stack<Character>();
        int len = s.length();
        int i = 0;
        for(; i < len / 2; i++){
            stack.push(s.charAt(i));
        }

        i = (len % 2 == 0) ? i : i+1; //skip the middle char if odd length

        //check if palindrome by checking if the halves at two direction are the same
        for(; i < len; i++){
            Character c = stack.pop();
            System.out.println(""+c+s.charAt(i));
            if (!c.equals(s.charAt(i))){
                System.out.println(""+c + s.charAt(i));
                return false;
            }
        }

        return stack.empty(); //if not empty, then not palindrome
    }
}