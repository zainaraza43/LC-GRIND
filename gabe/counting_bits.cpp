class Solution {
public:
    vector<int> countBits(int n) {

        vector<int> ans(n+1, 0);

        if (n == 0) return ans;

        ans[1] = 1;

        int s = 2, f = 4, i = 2;

        while(i <= n){
            if(i >= f) {
                s = f;
                f *= 2;
            }

            ans[i] = i < (s+f)/2 ? ans[i - (f-s)/2] : ans[i - (f-s)/2] + 1;

            i++;
        }

        return ans;
    }
};