# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        stringStack = []
        for char in range(len(s)):
            if s[char] == '(' or s[char] == '{' or s[char] == '[':
                stringStack.append(s[char])
            elif s[char] == ')' and stringStack and stringStack[-1] == '(':
                stringStack.pop()
            elif s[char] == '}' and stringStack and stringStack[-1] == '{':
                stringStack.pop()
            elif s[char] == ']' and stringStack and stringStack[-1] == '[':
                stringStack.pop()
            else:
                return False
        if not stringStack:
            return True
        else:
            return False
