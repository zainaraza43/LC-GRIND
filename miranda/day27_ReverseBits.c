uint32_t reverseBits(uint32_t n) {
    uint32_t reversed = 0b0;

    for (int i = 0; i < 32; i++) {
        uint32_t bit = (n >> i) & 1;
        reversed = reversed | (bit << 31 - i);
    }

    return reversed;
}