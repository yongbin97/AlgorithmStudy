import java.util.*;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        int answer = 0;

        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        for (int n : nums) pq.offer(n);

        for (int i = 0; i < k; i++) {
            answer = pq.poll();
        }
        return answer;
    }
}