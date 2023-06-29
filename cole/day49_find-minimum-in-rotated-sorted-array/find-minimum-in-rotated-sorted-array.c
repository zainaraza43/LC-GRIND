int findMin(int* nums, int numsSize) {
    int lo, m, hi;
    lo = 0, hi = numsSize - 1;
    if (nums[lo] < nums[hi])
        return nums[lo];
    while (lo != hi) {
        m = (lo + hi) / 2;
        if (nums[m] > nums[m + 1])
            lo = hi = m + 1;
        else if (nums[lo] > nums[m])
            hi = m;
        else
            lo = m + 1;
    }
    return nums[lo];
}
