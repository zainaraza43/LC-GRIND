import java.util.Arrays;

class CountingBits {
	public int[] countBits(int n) {
		int[] r = new int[n + 1];
		r[0] = 0;
		for (int i = 1; i < n + 1; i++) {
			r[i] = r[i >> 1] + (i & 0b1);
		}
		return r;
	}

	public static void main(String []args) {
		CountingBits s = new CountingBits();

		System.out.println(Arrays.toString(s.countBits(20)));
	}
}

