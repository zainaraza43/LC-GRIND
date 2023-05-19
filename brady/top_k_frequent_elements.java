class Solution {
  
    // O(n) time, O(n) space where n is the length of nums
    public int[] topKFrequent(int[] nums, int k) {
        // Count the frequencies of each num
        Map<Integer, Integer> frequencies = new HashMap<>();
        for (int num : nums) {
            int oldFrequency = frequencies.getOrDefault(num, 0);
            frequencies.put(num, oldFrequency+1);
        }

        // Add the mappings of nums to frequencies to a maxHeap using the frequencies as a Comparator in their 
        // PriorityQueue implementation. Then pop off the k highest priority nums.
        PriorityQueue<Pair<Integer, Integer>> maxHeap = new PriorityQueue<>(
            nums.length, Comparator.comparing(Pair<Integer, Integer>::getValue).reversed());
        for (Map.Entry<Integer, Integer> entry : frequencies.entrySet())
            maxHeap.add(new Pair<>(entry.getKey(), entry.getValue()));

        int[] kMostFrequent = new int[k];
        for (int i = 0; i < k; ++i) kMostFrequent[i] = maxHeap.poll().getKey();

        return kMostFrequent;
    }
}
