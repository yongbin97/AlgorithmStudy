import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.PriorityQueue;


class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        
        Arrays.sort(book_time, (o1, o2) -> {
            if (o1[0].equals(o2[0])) return o1[1].compareTo(o2[1]);
            else return o1[0].compareTo(o2[0]);
        });
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (String[] time: book_time){
            int start = convertTimeStr2Int(time[0]);
            int end = convertTimeStr2Int(time[1]) + 10;
            
            if (!pq.isEmpty() && pq.peek() <= start){
                pq.poll();
            }
            pq.offer(end);
            answer = Math.max(answer, pq.size());
        }
        
        return answer;
    }
    
    public int convertTimeStr2Int(String strTime){
        return Integer.parseInt(strTime.split(":")[0]) * 60 + Integer.parseInt(strTime.split(":")[1]);
    }
}