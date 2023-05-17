/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

// by removing the lowest set bit, we get a number that is:
// 1. lower than the current position (use DP)
// 2. has one less bit than the current position

int *countBits(int n, int *returnSize)
{
    int *ret = (int *)calloc(n + 1, sizeof(int));
    for (int i = 1; i <= n; ++i)
        ret[i] = ret[i & (i - 1)] + 1;
    *returnSize = n + 1;
    return ret;
}