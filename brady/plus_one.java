class Solution {
  
    // O(n) time, O(n) space
    public int[] plusOne(int[] digits) {
        int sum;
        for (int i = digits.length-1; i >= 0; --i) {
            ++digits[i];
            if (digits[i] <= 9) return digits;
            digits[i] = 0;
        }

        if (digits[0] == 0) {
            int[] newDigits = new int[digits.length+1];
            newDigits[0] = 1;
            return newDigits;
        }

        return digits;
    }
}
