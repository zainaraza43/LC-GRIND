class Solution {
  
    // O(n) time, O(1) space
    public int maxProfit(int[] prices) {
        int minVal = prices[0];
        int minIndex = 0;
        int maxProfit = 0;
        for (int i = 1; i < prices.length; ++i) {
            if (prices[i] < minVal) {
                minVal = prices[i];
                minIndex = i;
            } else {
                maxProfit = Math.max(maxProfit, prices[i] - minVal);
            }
        }
        return maxProfit;
    }
}
