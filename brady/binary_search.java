class Solution {
  
    // O(lg(n)) time, O(1) space
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        int m;

        while (l <= r) {
            m = l+((r-l)/2);    // Avoids overflow
            if (nums[m] == target) return m;
            else if (nums[m] < target) l = m+1;
            else r = m-1;
        }
        return -1;
    }
}
