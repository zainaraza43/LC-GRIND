class Solution:
    def hammingWeight(self, n: int) -> int:
        numOfOnes = 0
        while n:
            numOfOnes += n % 2
            n = n >> 1
        return numOfOnes
    
n = 0b00000000000000000000000000001011
solution = Solution()
print(solution.hammingWeight(n))