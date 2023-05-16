class Solution {
  
    // O(idk, i dont wanna go read number theory notes) time, O(once again, idk) space
    public boolean isHappy(int n) {
        Set<Integer> sums = new HashSet<>();
        while (true) {
            int sum = 0;
            while (n > 0) {
                int digit = n % 10;
                sum += digit * digit;
                n /= 10;
            }
            
            if (sum == 1) return true;
            if (sums.contains(sum)) return false;

            sums.add(sum);
            n = sum;
        }
    }
}
