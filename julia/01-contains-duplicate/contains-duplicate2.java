/*
 * Given an integer array nums, 
 * return true if any value appears at least twice in the array, 
 * and return false if every element is distinct. 
 * Eg. Input: nums = [1,2,3,1]
 * Output: true
 */

class Solution {
    public boolean containsDuplicate(int[] nums) {
        int arraySize = nums.length;
        int dupe;
        // Sort the array so you find duplicates immediately after they occur
        Arrays.sort(nums);
        // arraySize - 1 because we are eventually comparing the second last element to the last element and dont want to exceed the bounds.
        for(int i = 0; i < arraySize-1; i++){
            dupe = nums[i];
            if(dupe == nums[i+1]){
                return true;
            }
        }
        return false;
    }
}
