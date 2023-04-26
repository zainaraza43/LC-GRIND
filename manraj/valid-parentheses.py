class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(" or c == "[" or c == "{": stack.append(c)
            else:
                if not stack: return False
                pop = stack.pop()
                if c == ")" and pop != "(": return False
                if c == "]" and pop != "[": return False
                if c == "}" and pop != "{": return False
        
        return not stack
            

