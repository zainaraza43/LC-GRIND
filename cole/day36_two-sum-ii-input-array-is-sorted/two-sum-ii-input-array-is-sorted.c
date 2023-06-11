/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int *ret = (int *) malloc(2 * sizeof(int));
    int a = 0, b = numbersSize - 1, x;
    while ((x = numbers[a] + numbers[b]) != target){
        if (x < target) ++a;
        else --b;
    }
    *ret = a + 1;
    *(ret + 1) = b + 1;
    *returnSize = 2;
    return ret;
}
