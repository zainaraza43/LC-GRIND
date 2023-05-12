class PlusOne {
    public int[] plusOne(int[] digits) {
        int carry = 0;
        digits[digits.length-1]+=1;
        for (int i = digits.length - 1; i >= 0; i--) {
            digits[i] = digits[i] + carry;
            carry = digits[i] >= 10 ? digits[i] / 10 : 0;
            digits[i] %= 10;
        }

        if (carry != 0) {
            int []result = new int[digits.length+1];
            result[0] = carry;
            for (int i = 0; i < digits.length; i++) {
                result[i+1] = digits[i];
            }
            System.out.println(Arrays.toString(result));
            return result;
        }
        return digits;
    }
}
