class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int h = nums.size()-1;
        int m = (l+h)/2;

        while(l <= h) {
            if(target < nums[m]) {
                h = m-1;
            } else if (target == nums[m]) {
                return m;
            } else {
                l = m + 1;
            }

            m = (l+h)/2;
        }
        return -1;
    }
};