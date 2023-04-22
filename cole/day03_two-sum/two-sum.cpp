// beats 98.97%

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> cache;
        cache.reserve(nums.size());
        auto pos = 0;
        for (const auto &num : nums)
        {
            auto it = cache.find(target - num);
            if (it != cache.end())
            {
                return vector<int>{cache[target - num], pos};
            }
            cache[num] = pos++;
        }
        return vector<int>();
    }
};