/* Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. */

int cmpF(int *num1, int *num2){
    return *num1-*num2;
}

bool containsDuplicate(int* nums, int numsSize){
    
    qsort(nums, numsSize, sizeof(int), cmpF);
    for (int i=0; i<numsSize-1; i++)
    {
        if (nums[i]==nums[i+1]) return true;
    }
    return false;
}

/* Explanation
   First I created a custom function cmpF which takes two pointers to integers and returns the difference. If the difference is is positive, num1 is greather than num2,
   if the difference is negative, num1 is less than num2, if the difference is 0, num1 is equal to num2.
   
   qsort() sorts the array in ascending order
   
   The for loop iterates over the array, if nums[i] is equal to the integer next to it num[i+1], we return true. Otherwise, return false.

*/
