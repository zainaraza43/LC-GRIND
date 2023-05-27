class Solution:
    def __init__(self):
        self.mem = {}
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        
        if self.mem.get(n):
            return self.mem.get(n)
        
        self.mem[n] = (n&0b1) + self.hammingWeight(n>>1)
        return self.mem[n]
