class Solution {
public:
    int climbStairs(int n) {
        if (n == 1 || n == 2) return n;
        
        vector<int> stairsOf(n);
        
        stairsOf[0] = 1;
        stairsOf[1] = 2;
        
        for(int i = 2; i < n; ++i) {
            stairsOf[i] = stairsOf[i-1] + stairsOf[i-2];
        }
        
        return stairsOf[n-1];
        
    }
};