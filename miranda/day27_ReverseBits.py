class Solution:
    def reverseBits(self, n: int) -> int:
        reversed = 0
        for i in range(32):
            bit = (n >> i) & 1
            reversed = reversed | (bit << 31 - i)
        return reversed
    
n = 0b11111111111111111111111111111101
solution = Solution()
print(solution.reverseBits(n))