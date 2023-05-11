class KthLargest {

    private int k;
    private ArrayList<Integer> nums;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.nums = new ArrayList<Integer>();
        for (int num : nums) this.nums.add(num);
        Collections.sort(this.nums);    // Sort the arraylist in ascending order
    }
    
    public int add(int val) {
        // Find where to insert the value using binary search
        int l = 0;
        int r = nums.size() - 1;
        int m = 0;

        while (l <= r) {
            m = l+(r-l)/2;
            if (val == nums.get(m)) {
                nums.add(m, val);
                return nums.get(nums.size() - k);
            } else if (val < nums.get(m)) {
                r = m-1;
            } else {
                l = m+1;
            }
        }

        // If the binary search was exhausted...
        if (l > m) nums.add(m+1, val);  // If the last step was moving the left bound to the right
        else nums.add(m, val);        // If the last step was moving the right bound to the left

        return nums.get(nums.size() - k);
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
