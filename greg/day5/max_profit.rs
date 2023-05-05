impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut max_profit = 0;
        let mut min_price = std::i32::MAX;
        for price in prices {
            if price < min_price {
                min_price = price;
            } else if price - min_price > max_profit {
                max_profit = price - min_price;
            }
        }
        return max_profit;
    }
}