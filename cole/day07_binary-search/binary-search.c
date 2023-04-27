// faster 72% solution

int search(int *nums, int numsSize, int target)
{
    int *lo = nums, *hi = nums + numsSize - 1;
    if (*lo == target)
        return 0;
    if (*hi == target)
        return numsSize - 1;
    for (int *med; lo != hi;)
    {
        med = lo + ((hi - lo) / 2);
        if (*med == target)
            return (med - nums);
        if (*med < target)
            lo = med + 1;
        else
            hi = med;
    }
    return (*lo == target) ? (lo - nums) : -1;
}

// simple, "correct" solution

int search(int *nums, int numsSize, int target)
{
    int lo = 0, hi = numsSize - 1;
    for (int med; lo != hi;)
    {
        med = (hi + lo) / 2;
        if (nums[med] < target)
            lo = med + 1;
        else
            hi = med;
    }
    return (nums[lo] == target) ? lo : -1;
}