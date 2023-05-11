class Solution:
    def __init__(self):
        self.mem = [0, 1, 2, 3]
        
    def climbStairs(self, n: int) -> int:
        for i in range(4, n+1):
            self.mem.append(self.mem[-1]+self.mem[-2])
        
        return self.mem[n]


if __name__ == '__main__':
    s = Solution()

    for i in range(10):
        print(i+1, s.climbStairs(i+1))
