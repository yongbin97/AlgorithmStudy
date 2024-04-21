import java.util.*;

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Deque<Integer> dq = new ArrayDeque<>();
        int[] result = new int[temperatures.length];

        for (int i = 0; i < temperatures.length; i ++){
            while (!dq.isEmpty() && temperatures[dq.peek()] < temperatures[i]){
                result[dq.peek()] = i - dq.peek();
                dq.pop();
            }
            dq.push(i);
        }

        return result;
    }
}