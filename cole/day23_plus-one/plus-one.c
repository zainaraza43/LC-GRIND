/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize){
    int *ret, *cp;
    int *it = digits, *rit = digits + digitsSize - 1;
    const int *rend = it - 1;
    for (; rit != rend && *rit == 9; --rit)
        ;;
    *returnSize = digitsSize + (rit == rend);
    ret = (int *) calloc(*returnSize, sizeof(int));
    if (rit == rend)
    {
        *ret = 1;
        return ret;
    }
    cp = ret;
    while (it < rit)
    {
        *cp = *it;
        ++cp;
        ++it;
    }
    *cp = *it + 1;
    return ret;
}