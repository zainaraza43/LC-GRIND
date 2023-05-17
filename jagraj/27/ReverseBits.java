public class ReverseBits {
	// you need treat n as an unsigned value
	public int reverseBits(int n) {
		int r = 0;
		for (int i = 0; i < 32; i++) {
			r = r << 1;
			int b = n & 0b1;
			r = r | b;
			r = r & (0b11111111111111111111111111111110 | b);
			n = n >> 1;
		}
		return r;
	}

}
