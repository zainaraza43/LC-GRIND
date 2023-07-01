template<typename T>
struct comparator {

    bool operator()(const T& l, const T& r) {
        return l.second > r.second;
    }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;

        for(auto num: nums) {
            count[num] += 1;
        } 

        priority_queue<pair<int, int>, vector<pair<int,int>>, comparator<pair<int, int>>> pq;

        for(auto p: count) {
            pq.push(p);
            if (pq.size() > k) {
                pq.pop();
            }
        }
        vector<int> ans;

        for(int i = 0; i < k; i++) {
            ans.push_back(pq.top().first);
            pq.pop();
        }

        reverse(ans.begin(), ans.end());

        return ans;
    }
};