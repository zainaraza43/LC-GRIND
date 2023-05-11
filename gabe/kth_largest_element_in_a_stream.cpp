class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) : k_(k) {
        pq.push(-pow(10, 4) - 1);

        for (int i = 0; i < nums.size(); i ++) {
            pq.push(nums[i]);

            if (pq.size() > k_) {
                pq.pop();
            }
        }


    }
    
    int add(int val) {

        if (val < pq.top() && pq.size() == k_) {
            return pq.top();
        }

        pq.push(val);
        if (pq.size() > k_) {
            pq.pop();
        }

        return pq.top();
    }

private:
    int k_;
    priority_queue<int, vector<int>, greater<int>> pq;
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */