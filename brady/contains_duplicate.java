import java.util.Arrays;

class Solution {
  
    // O(n) time (disregarding collisions), O(n) space
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> foundNums = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (foundNums.contains(nums[i])) {
                return true;
            }
            foundNums.add(nums[i]);
        }
        return false;
    }
}
