#include <stdio.h>

int maxProfit(int *prices, int pricesSize) {
	if (pricesSize == 1) {
		return 0;
	}

	int max = prices[pricesSize - 1];
	int diff = 0;

	for (int i = pricesSize - 2; i >= 0; i--) {
		diff = diff > max - prices[i] ? diff : max - prices[i];
		max = max > prices[i] ? max : prices[i];
	}
	return diff < 0 ? 0 : diff;
}

int main() {
	int prices1[] = {7, 1, 5, 3, 6, 4};
	printf("%d\n", maxProfit(prices1, 6));
	int prices2[] = {7, 6, 4, 3, 2, 1};
	printf("%d\n", maxProfit(prices2, 6));
}
