import java.util.*;
import java.util.stream.Collectors;


class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = Arrays.stream(scoville)
            .boxed()
            .collect(Collectors.toCollection(PriorityQueue::new));
        
        while (pq.size() > 1 && pq.peek() < K){
            int f1 = pq.poll();
            int f2 = pq.poll();

            pq.add(f1 + f2 * 2);
            answer ++;
            
        }
        
        if (pq.peek() < K) return -1;
        else return answer;
    }
}