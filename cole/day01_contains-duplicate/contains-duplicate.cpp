// beats 97.60%

#include <unordered_set>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> m;
        m.reserve(nums.size());
        for (auto it = nums.begin(); it != nums.end() && m.insert(*it).second; ++it);
        return m.size() != nums.size();
    }
};
