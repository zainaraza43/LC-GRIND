class Solution {
  
    // O(n) time, O(1) space
    public int missingNumber(int[] nums) {
        // using short because n <= 10000 < 2^15 - 1

        // XOR all the nums, and all the numbers from 0 to nums.length (inclusive)
        short allNums = 0;
        short actual = 0;
        for (short i = 0; i < nums.length; ++i) {
            allNums ^= i;
            actual ^= nums[i];
        }
        allNums ^= nums.length;

        return allNums ^ actual;
    }
}
