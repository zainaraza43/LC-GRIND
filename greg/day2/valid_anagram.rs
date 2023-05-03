impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        use std::collections::HashMap;
        let mut map = HashMap::new();
        for c in s.chars() {
            let count = map.entry(c).or_insert(0);
            *count += 1;
        }
        for c in t.chars() {
            let count = map.entry(c).or_insert(0);
            *count -= 1;
        }
        for (_, v) in map {
            if v != 0 {
                return false;
            }
        }
        return true;
    }
}