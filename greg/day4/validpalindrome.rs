impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let chars = s.to_lowercase().chars().filter(|c| c.is_alphanumeric()).collect::<String>();
        return chars == chars.chars().rev().collect::<String>();
    }
}