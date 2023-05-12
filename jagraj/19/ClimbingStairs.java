public class ClimbingStairs {
    private int[] poop;

    public ClimbingStairs() {
        this.poop = new int[46];
        for (int i = 0; i <= 3; i++) this.poop[i] = i;
    }

    public int climbStairs(int n) {

        for (int i = 4; i <= n; i++) {
            this.poop[i] = this.poop[i-1]+this.poop[i-2];
        }
        return this.poop[n];
    }
}
