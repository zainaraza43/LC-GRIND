class Solution {
    
    // O(n) time, O(1) space
    public int minCostClimbingStairs(int[] cost) {
        // Edge case for small number of steps. Since you can start from index 1, if there is only 1 step I assume we can
        // just skip it
        if (cost.length < 2) return 0;

        // Recurrence:
        // solutions[n-1] = cost[n-1]
        // solutions[n-2] = cost[n-2]
        // solutions[i] = cost[i] + min(solutions[i+1], solutions[i+2]) for i < n-2
        // Only need to store the previous two solutions for less memory usage
        int twoBefore = cost[cost.length-1];
        int oneBefore = cost[cost.length-2];
        int nextVal;
        for (int i = cost.length-3; i >= 0; --i) {
            nextVal = cost[i] + Math.min(oneBefore, twoBefore);
            twoBefore = oneBefore;
            oneBefore = nextVal;
        }

        return Math.min(oneBefore, twoBefore);
    }
}
