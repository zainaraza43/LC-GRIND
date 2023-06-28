class Solution:
    def isValid(self, s: str) -> bool:
        close_dict = {')': '(', ']': '[', '}': '{'}
        closed = [')', ']', '}']
        openStack = []

        if len(s) % 2 == 0:
            for i in range(0, len(s)):
                if s[i] in closed and len(openStack) != 0:
                    if openStack[-1] == close_dict[s[i]]:
                        openStack.pop()
                    else:
                        return False
                elif s[i] not in closed:
                    openStack.append(s[i])
                else:
                    return False
        else:
            return False

        if len(openStack) == 0:
            return True
        
        return False
