# beats 84%

class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        o = {'{':'}', '(':')', '[':']'}
        c = {'}':'{', ')':'(', ']':'['}
        for ch in s:
            if ch in o:
                l.append(ch)
            if ch in c:
                if not l or l[-1] != c[ch]:
                    return False
                l.pop()
        return not l