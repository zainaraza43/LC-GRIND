// the xor solution
int missingNumber(int *nums, int numsSize)
{
    int res = numsSize;
    for (int i = 0; i < numsSize; i++)
    {
        res ^= i;
        res ^= nums[i];
    }
    return res;
}

// the sum solution
int missingNumber(int *nums, int numsSize)
{
    int sum = 0;
    for (int *it = nums, *end = nums + numsSize; it < end; ++it)
    {
        sum += *it;
    }
    return (numsSize * (numsSize + 1) / 2) - sum;
}
