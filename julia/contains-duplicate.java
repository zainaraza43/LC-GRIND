class Solution {
    public boolean containsDuplicate(int[] nums) {
        int arraySize = nums.length;
        int dupe;
        // start at [0], then check [1]
        for(int i = 0; i < arraySize; i++){
          dupe = nums[i];
            // check [0] against [1],[2],[...]
            for(int j = i+1; j < arraySize; j++){
                if(dupe == nums[j]){
                  return true;
                }
            }
        }
        return false;
    }
}