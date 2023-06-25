# the slow but easy python solution
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 2
        while len(tokens) > 1:
            if tokens[i] in '+-*/':
                expr = f'({tokens[i-2]}){tokens[i]}({tokens[i-1]})'
                tokens = tokens[:i-2] + [int(eval(expr))] + \
                    (tokens[i+1:] if i < len(tokens) - 1 else [])
                i -= 2
            i += 1
        return int(tokens[0])
