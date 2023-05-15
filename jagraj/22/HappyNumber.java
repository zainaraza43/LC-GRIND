class HappyNumber {
	private int sumDigits(int n) {
		int s = 0;
		while (n != 0) {
			s += (n % 10) * (n % 10);
			n /= 10;
		}
		return s;
	}

	public boolean isHappy(int n) {
		short[] seen = new short[101];

		int s = 0;
		while (true) {
			if (n < 100) {
				seen[s] = 1;
			}
			s = this.sumDigits(n);

			n = s;
			if (n < 100 && seen[n] == 1 || n == 1) {
				break;
			}

		}
		return n == 1;
	}
}
