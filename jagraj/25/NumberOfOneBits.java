public class NumberOfOneBits {

	public int hammingWeight(int n) {
		int r = 0;
		while (n != 0) {
			r += n & 0b1;
			n = (n >> 1) & 0b01111111111111111111111111111111;
		}
		return r;
	}

	public static void main(String[] args) {
		NumberOfOneBits s = new NumberOfOneBits();

		System.out.println(s.hammingWeight(0b00000000000000000000000000001011));
		System.out.println(s.hammingWeight(0b00000000000000000000000010000000));
		System.out.println(s.hammingWeight(0b11111111111111111111111111111101));
	}
}
