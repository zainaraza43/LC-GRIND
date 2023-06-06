class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> seen;

        while(n != 1) {
            if (seen.count(n) != 0) return false;
            seen.insert(n);
            n = sumSquares(n);
        } 

        return true;
    }

    int sumSquares(int n) {
        int sum = 0;

        while (n > 0) {
            sum += pow(n % 10, 2);
            n /= 10;
        }

        return sum;
    }
};