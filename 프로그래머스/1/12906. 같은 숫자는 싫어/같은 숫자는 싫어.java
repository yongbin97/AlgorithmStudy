import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> answerList = new ArrayList<>();
        
        int last = -1;
        
        for (int num: arr) {
            if (num != last) {
                last = num;
                answerList.add(num);
            }
        }
        

        return answerList.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}