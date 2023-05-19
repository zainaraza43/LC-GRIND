class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0, iter_max = -1, init=0, min = *(prices.begin());
        //vector<int> prices_copy = prices;
        //reverse(prices_copy.begin(), prices_copy.end());
        //if ( ! is_sorted(prices_copy.begin(), prices_copy.end()) ) {
        if ( prices.size() > 1 ){
        vector<int> to_comp(prices.begin()+1, prices.end());
        sort(to_comp.begin(), to_comp.end());
        iter_max = *(to_comp.end() - 1);
        auto ptr = to_comp.end() - 1;
        for (auto it = prices.begin(); it != prices.end()-1; it++) {
            if ( iter_max > *it || init == 0) {
               init=1;
               if ( *it > min )
                  continue;
               else if ( *it == min ) {
                  if ( !max && iter_max > *it )
                     max = iter_max - *it;
                  continue;
               } else
                  min = *it;
               vector<int> tmp(it+1, prices.end());
               sort(tmp.begin(), tmp.end());
               iter_max = *(tmp.end() - 1);
               if ( iter_max - *it > max )
                  max = iter_max - *it;
            } else {
                if ( ptr != to_comp.begin()) {
                   ptr--;
                   iter_max = *ptr;
                }
            }
        }
        }
        //}
      
        return max;
    }
};
