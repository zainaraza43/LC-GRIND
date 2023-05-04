import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> val = new HashMap<Integer, Integer>(); //value, index
        for (int i = 0; i < nums.length; i++) {
            int comp = target - nums[i];
            if (val.containsKey(comp)){
                return new int [] {val.get(comp), i}; //the complement is the earlier / smaller index
            }
            else{
                val.put(nums[i], i); //add all scanned elements
            }
        }

        return new int [] {-1, -1}; //one valid answer exists, so won't reach here in theory
    }
}