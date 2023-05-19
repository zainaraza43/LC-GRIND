class Solution {
    
    // O(n) time, O(n) space
    public int[] countBits(int n) {
        int[] ans = new int[n+1];

        // Recurrence:
        // ans[0] = 0
        // ans[1] = 1
        // ans[i] = 1 + ans[i minus the current highest power of 2 reached by the loop index]
        int curHighestPowerOf2 = 1;
        ans[0] = 0;

        // Edge case for where n = 0
        if (n == 0) return ans;

        ans[1] = 1;
        for (int i = 2; i < n+1; ++i) {
            if (i % curHighestPowerOf2 == 0) curHighestPowerOf2 = i;
            ans[i] = 1 + ans[i-curHighestPowerOf2];
        }

        return ans;
    }
}
