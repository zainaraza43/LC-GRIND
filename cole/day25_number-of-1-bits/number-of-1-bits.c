int hammingWeight(uint32_t n)
{
    int count = n & 1;
    for (; n >>= 1; ++count)
        n &= (n - 1);
    return count;
}