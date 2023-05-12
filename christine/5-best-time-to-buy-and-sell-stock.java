class Solution {
    public int maxProfit(int[] prices) {
        int maxP = 0;
        int buyDay = prices[0];
        for (int i = 1; i < prices.length; i++){
            if (prices[i] < buyDay){
                buyDay = prices[i];
            }

            if (prices[i] - buyDay > maxP){//keep track of max profit so far (regardless buyday)
                maxP = prices[i] - buyDay;
            }
        }

        return maxP;
    }
}
