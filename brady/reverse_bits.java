public class Solution {
    // you need treat n as an unsigned value
    // O(1) time, O(1) space
    public int reverseBits(int n) {
        int rev = 0;
        // For all 32 bits, shift them to their desired position in a temp value then bitwise OR them into rev
        for (int i = 0; i < 32; ++i) {
            rev |= (n & 1) << (31 - i); // (n & 1) is the rightmost bit and << (31 - i) moves it to its desired position
            n >>= 1;    // Take off the last bit by right shifting so we can use the next last bit
        }
        return rev;
    }
}
