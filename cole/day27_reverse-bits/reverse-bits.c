uint32_t reverseBits(uint32_t n)
{
    uint32_t m = 0;
    for (int8_t i = 0; i < 32; ++i)
    {
        m = 2 * m + n % 2;
        n /= 2;
    }
    return m;
}