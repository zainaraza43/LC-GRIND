class Solution {
  
    // O(nlg(n)) time, O(n) space
    public int lastStoneWeight(int[] stones) {
        // Empty edge case
        if (stones.length == 0) return 0;

        // Store the stones in a min-heap
        List<Integer> maxHeap = new ArrayList<>(stones.length);
        for (int stone : stones) {
            insertNode(maxHeap, stone);
        }

        // Smash the stones iteratively
        while (maxHeap.size() > 1) {
            insertNode(maxHeap, Math.abs(extractNode(maxHeap)-extractNode(maxHeap)));
        }

        return maxHeap.get(0);
    }
  
    // Parent index: (i-1)/2
    // Left child index: 2i+1
    // Right child index: 2i+2

    private void insertNode(List<Integer> maxHeap, int node) {
        maxHeap.add(node);
        for (int i = maxHeap.size()-1; i > 0; i = (i-1)/2) {
            if (maxHeap.get((i-1)/2) >= maxHeap.get(i)) return;
            swap(maxHeap, i, (i-1)/2);
        }
    }
  
    private int extractNode(List<Integer> maxHeap) {
        swap(maxHeap, 0, maxHeap.size()-1);
        int extractedNode = maxHeap.remove(maxHeap.size()-1);

        // Heapify
        for (int i = 0; (2*i)+1 < maxHeap.size();) {
            // Left child is in the for loop condition so it must exist
            int leftVal = maxHeap.get((2*i)+1);
            int rightVal = (2*i)+2 < maxHeap.size() ? maxHeap.get((2*i)+2) : Integer.MIN_VALUE;
            if (Math.max(leftVal, rightVal) > maxHeap.get(i)) {
                if (leftVal > rightVal) {
                    swap(maxHeap, i, (2*i)+1);
                    i = (2*i)+1;
                } else {
                    swap(maxHeap, i, (2*i)+2);
                    i = (2*i)+2;
                }
            } else return extractedNode;
        }

        return extractedNode;
    }

    private void swap(List<Integer> maxHeap, int i1, int i2) {
        int temp = maxHeap.get(i1);
        maxHeap.set(i1, maxHeap.get(i2));
        maxHeap.set(i2, temp);
    }
}
