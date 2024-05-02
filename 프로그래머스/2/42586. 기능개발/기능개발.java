import java.util.*;


class Solution {
    public int getTime(int progress, int speed){
        return (int) Math.ceil((double) (100 - progress) / (double) speed);
    }
    
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        
        int curr = 0;
        int pointer = 0;
        while (pointer < progresses.length){
            while (pointer < progresses.length && getTime(progresses[curr], speeds[curr]) >= getTime(progresses[pointer], speeds[pointer])){
                pointer ++;
            }
            answer.add(pointer - curr);
            curr = pointer;
        }
        
        
        return answer.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}