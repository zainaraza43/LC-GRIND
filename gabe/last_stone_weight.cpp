class Solution {
public:
    priority_queue<int> pq;

    int lastStoneWeight(vector<int>& stones) {
        for(int stone: stones) {
            pq.push(stone);
        }

        int x, y;
        while (pq.size() > 1) {
            y = pq.top();
            pq.pop();
            x = pq.top();
            pq.pop();

            if (y > x) pq.push(y - x);
        }

        if (pq.size() == 1) return pq.top();

        return 0;
    }


};