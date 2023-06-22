from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [];

        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(char))

        return stack.pop()