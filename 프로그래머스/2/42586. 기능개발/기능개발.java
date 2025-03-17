import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        /**
        progress / speed = time
        */
        List<Integer> answer = new ArrayList<>();
        
        int size = progresses.length;
        int time = 0;
        int count = 0;
        
        for (int i = 0; i < size; i++) {
            int curr = (100 - progresses[i]) / speeds[i];
            if ((100 - progresses[i]) % speeds[i] > 0) {
                curr += 1;
            } 
            
            if (count > 0 && curr > time) {
                answer.add(count);
                count = 0;
            } 
            
            time = Math.max(time, curr);
            count += 1;
        }
        
        answer.add(count);
        
        return answer.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}