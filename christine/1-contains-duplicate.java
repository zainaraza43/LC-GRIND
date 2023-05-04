import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> values = new HashSet<Integer>();
        int len = nums.length;
        for(int i = 0; i < len; i++){
            if(!values.contains(nums[i])){ //the int at nums[i] is unique
                values.add(nums[i]);
            }
            else{//contains duplicate
                return true;
            }
        }

        return false;
    }
}