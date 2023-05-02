class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        if ( nums.size() == 2 ) {
            return {0,1};
        } else if ( nums.size() <= 500 ) {
            for ( int it = 0; it + 1 < nums.size(); it++ ) {
                for ( int jt = nums.size() - 1; jt > it; jt-- ) {
                    if ( nums[it] + nums[jt]  == target ) {
                        return {it, jt};
                    }
                }
            }
        } else {
            unordered_map<int,int> map;
            for(int i=0;i<nums.size();i++){
               if(map.count(target-nums[i])>0) return {map[target-nums[i]],i};
               map[nums[i]]=i; 
            }
        }
        return {};
    }
};
