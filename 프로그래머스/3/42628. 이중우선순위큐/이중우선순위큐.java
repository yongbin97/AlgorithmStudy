import java.util.*;

class Solution {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>(Comparator.naturalOrder());
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        
        for (String op: operations){
            String[] opArr = op.split(" ");
            operate(opArr[0], Integer.parseInt(opArr[1]));
        }
        
        if (!minHeap.isEmpty()){
            answer[0] = maxHeap.poll();
            answer[1] = minHeap.poll();
        }
        
        return answer;
    }
    
    public void operate(String op, int num){
        if (op.equals("I")){
            minHeap.add(num);
            maxHeap.add(num);
        } else {
            if (num == 1){
                minHeap.remove(maxHeap.poll());
            } else {
                maxHeap.remove(minHeap.poll());
            }
        }
    }
}