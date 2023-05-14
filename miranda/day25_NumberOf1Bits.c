int hammingWeight(uint32_t n) {
    int numOfOnes = 0;
    while(n > 0) {
        n = n & (n-1);
        numOfOnes++;
    }
    return numOfOnes;   
}