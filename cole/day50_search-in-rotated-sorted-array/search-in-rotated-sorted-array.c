// modified solution to https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
int findMinIndex(int* nums, int numsSize) {
    int lo, m, hi;
    lo = 0, hi = numsSize - 1;
    if (nums[lo] < nums[hi] || numsSize < 2)
        return lo;
    while (lo != hi) {
        m = (lo + hi) / 2;
        if (nums[m] > nums[m + 1])
            lo = hi = m + 1;
        else if (nums[lo] > nums[m])
            hi = m;
        else
            lo = m + 1;
    }
    return lo;
}

#define IND(i) ((i + base) % numsSize)

int search(int* nums, int numsSize, int target) {
    int lo, m, hi, base, len;
    lo = 0, hi = numsSize - 1;
    base = findMinIndex(nums, numsSize);
    while (lo != hi) {
        m = (lo + hi) / 2;
        if (nums[IND(m)] < target)
            lo = m + 1;
        else
            hi = m;
    }
    return (nums[IND(lo)] == target ? IND(lo) : -1);
}