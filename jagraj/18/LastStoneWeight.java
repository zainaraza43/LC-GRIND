import java.util.Comparator;
import java.util.PriorityQueue;

public class LastStoneWeight {
	public int lastStoneWeight(int[] stones) {
		PriorityQueue<Integer> heap = new PriorityQueue<Integer>(Comparator.reverseOrder());

		for (int s : stones) {
			heap.add(s);
		}

		while (heap.size() > 1) {
			int x = heap.poll(), y = heap.poll();
			int z = x - y;

			if (z > 0) {
				heap.add(z);
			}
		}

		if (heap.size() == 1)
			return heap.peek();
		return 0;
	}

	public static void main(String[] args) {
		LastStoneWeight s = new LastStoneWeight();

		System.out.println(s.lastStoneWeight(new int[] { 2, 7, 4, 1, 8, 1 }));
		System.out.println(s.lastStoneWeight(new int[] { 1 }));
	}
}
