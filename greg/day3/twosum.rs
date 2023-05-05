impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        use std::collections::HashMap;
        let mut map = HashMap::new();
        for (i, n) in nums.iter().enumerate() {
            let diff = target - n;
            if map.contains_key(&diff) {
                return vec![*map.get(&diff).unwrap() as i32, i as i32];
            }
            map.insert(n, i);
        }
        return vec![];
    }
}