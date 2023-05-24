class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        
        int temp, a = cost[cost.size()-2], b = cost[cost.size()-1];

        for (int i = cost.size()-3; i >= 0; i--) {
            temp = a;
            a = cost[i] + min(a, b);
            b = temp;
        }

        return min(a, b);

    }
};