public class Solution {
  
    // O(1) time, O(1) space
    public int hammingWeight(int n) {
        // you need to treat n as an unsigned value
        int num1Bits = 0;
        while (n != 0) {
            num1Bits += n & 1;
            n >>>= 1;   // Logical right shift (>>>) to ignore sign
        }

        return num1Bits;
    }
}
