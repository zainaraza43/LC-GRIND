/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *productExceptSelf(int *nums, int numsSize, int *returnSize)
{
    *returnSize = numsSize;
    int *out = (int *)calloc(numsSize, sizeof(int));
    int zeros[2] = {0, 0}, product = 1, i;

    if (!nums[0])
    {
        zeros[0] = 1;
        zeros[1] = 0;
    }
    for (i = 1; i < numsSize; ++i)
    {
        if (!nums[i])
        {
            if (zeros[0])
                return out;
            zeros[0] = 1;
            zeros[1] = i;
        }
        else
        {
            product *= nums[i];
        }
    }

    if (zeros[0])
    {
        if (zeros[1] != 0)
            product *= *nums;
        out[zeros[1]] = product;
        return out;
    }
    *out = product;
    for (i = 1; i < numsSize; ++i)
    {
        product /= nums[i];
        product *= nums[i - 1];
        out[i] = product;
    }
    return out;
}