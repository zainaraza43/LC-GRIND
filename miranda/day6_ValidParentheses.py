from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for x, parenthesis in enumerate(s):
            #opening parenthesis cases
            if(parenthesis == "(" or parenthesis == "{" or parenthesis == "[" ):
                stack.appendleft(parenthesis)
            else:
                #closing parenthesis cases
                if(len(stack) == 0):
                    return False
                if(stack[0] == "(" and parenthesis != ")"):
                    return False
                elif(stack[0] == "{" and parenthesis != "}"):
                    return False
                elif(stack[0] == "]" and parenthesis != "]"):
                    return False
                stack.popleft()
        
        if (len(stack) == 0):
            return True
        return False

#driver code
s = "()"
solution = Solution()
print(solution.isValid(s))