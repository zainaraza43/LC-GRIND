// beats 98.25%

#define MIN(a, b) a < b ? a : b
#define MAX(a, b) a > b ? a : b

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        auto it = prices.begin();
        int min = *it, max = 0;
        while (++it != prices.end())
        {
            min = MIN(min, *it);
            max = MAX(max, *it - min);
        }
        return max;
    }
};