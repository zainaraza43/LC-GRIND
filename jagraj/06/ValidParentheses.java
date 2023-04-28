import java.util.*;

public class ValidParentheses {

	public boolean isValid(String s) {
		List<Character> open = new ArrayList<Character>(Arrays.asList(new Character[] { '(', '[', '{' }));
		List<Character> close = new ArrayList<Character>(Arrays.asList(new Character[] { ')', ']', '}' }));
		Stack<Character> stack = new Stack<Character>();

		if (s.length() <= 1) {
			return false;
		}

		stack.push(s.charAt(0));

		for (int i = 1; i < s.length(); i++) {
			char c = s.charAt(i);
			// check if s[i] is open bracket
			if (open.contains(c)) {
				// j = open.indexOf(c);
				stack.push(c);
			} else {
				int j = close.indexOf(c);
				if (stack.size() == 0 || (Character) stack.peek() != open.get(j)) {
					return false;
				}
				stack.pop();
			}
		}

		if (stack.size() != 0)
			return false;
		return true;
	}

	public static void main(String[] args) {
		ValidParentheses s = new ValidParentheses();

		System.out.println(s.isValid("()"));
		System.out.println(s.isValid("()[]{}"));
		System.out.println(s.isValid("(]"));
	}

}
