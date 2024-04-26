import java.util.*;


class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> {
            return o2[0] - o1[0];
        });
        
        for (int i = 0; i < prices.length; i++){
            if (!pq.isEmpty()){
                while (!pq.isEmpty() && pq.peek()[0] > prices[i]){
                    int[] element = pq.poll();
                    answer[element[1]] = i - element[1]; 
                }    
            }
            pq.offer(new int[]{prices[i], i});
        }
        
        while(!pq.isEmpty()){
            int[] element = pq.poll();
            answer[element[1]] = prices.length - element[1] - 1; 

        }        
        return answer;
    }
}