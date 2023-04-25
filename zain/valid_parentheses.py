def isValid(self, s: str) -> bool:
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []

    for c in s:
        if c in brackets.values():
            stack.append(c)
        elif not stack or stack.pop() != brackets[c]:
            return False
    return len(stack) == 0
