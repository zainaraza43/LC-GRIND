class Solution {
  
    // O(n) time, O(1) space
    public int climbStairs(int n) {
        // Edge cases for small n
        if (n < 2) return 1;

        // Recurrence:
        // solutions[0] = 1
        // solutions[1] = 1 + solutions[0] = 2
        // solutions[i] = solutions[i-1] + solutions[i-2]
        // We can use the fibonacci sequence starting from values 1 and 2
        int fib1 = 1;
        int fib2 = 2;
        for (int i = 2; i < n; ++i) {
            int nextVal = fib1 + fib2;
            fib1 = fib2;
            fib2 = nextVal;
        }

        return fib2;
    }
}
