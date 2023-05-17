class Solution {
  
    // O(n) time, O(1) space
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int num : nums) result ^= num; // XOR with all of the nums, each pair of duplicates will cancel each other out
        return result;
    }
}
