class Solution:
    def climbStairs(self, n):
        arr = [0, 1, 2]
        for i in range(3, n + 1):
            arr[0] = arr[1]
            arr[1] = arr[2]
            arr[2] = arr[0] + arr[1]
        return arr[2]
