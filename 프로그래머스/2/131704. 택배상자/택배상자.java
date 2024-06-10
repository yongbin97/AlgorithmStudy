import java.util.*;


class Solution {
    public int solution(int[] order) {
        int answer = 0;
        int idx = 1;
        Deque<Integer> sub = new ArrayDeque<>();
        
        for (int box: order){
            if (idx <= box){
                while(idx < box) {
                    sub.add(idx);
                    idx ++;
                }
                answer ++;                
                idx ++;
            } else {
                if (sub.isEmpty() || sub.getLast() != box) break; 
                
                while(!sub.isEmpty() && sub.getLast() == box){
                    sub.pollLast();
                    answer ++;
                }
            }
        }
        
        return answer;
    }
}