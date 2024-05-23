import java.util.Deque;
import java.util.ArrayDeque;


class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        Deque<Integer> dq = new ArrayDeque<Integer>();
        
        for (int i=numbers.length - 1; i >= 0; i --){
            int num = numbers[i];
            while (!dq.isEmpty() && num >= dq.getFirst()) {
                dq.poll();
            }
            if (!dq.isEmpty()){
                answer[i] = dq.getFirst();
            } else {
                answer[i] = -1;
            }
            dq.addFirst(num);
        }
        return answer;
    }
}