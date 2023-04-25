class Solution {
    public boolean containsDuplicate(int[] nums) {
        int arraySize = nums.length;
        int dupe;
        // start at [0], then check [1]
        for(int i = 0; i < arraySize; i++){
            // check [0] against [1],[2],[...] backwards
            for(int j = arraySize; j > 0; j--){
                dupe = nums[i];
                if(dupe == nums[j]){
                    System.out.println(true);
                }
            }
            if(dupe = nums[arraySize]){
                System.out.println(false);
            }
        }
    }
}