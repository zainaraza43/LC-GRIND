import java.util.Arrays;

// O(n) time, O(n) space
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> pairs = new HashMap<>();

        for (int i = 0; i < nums.length; ++i) {
            
            // Check if the difference (u.e., target-nums[i]) has already been found, and if so get its index
            int difference = target - nums[i];
            if (pairs.containsKey(difference)) {
                return new int[]{ pairs.get(difference), i };
            }

            // Add the number and its index to the map
            pairs.put(nums[i], i);
        }
        return null;
    }
}
