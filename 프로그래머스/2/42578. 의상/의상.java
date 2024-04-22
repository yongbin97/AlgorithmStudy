import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        Map<String, Integer> clothCountMap = new HashMap<>();
        
        for (String[] cloth: clothes){
            clothCountMap.put(cloth[1], clothCountMap.getOrDefault(cloth[1], 0) + 1);
        }
        
        for (Integer value: clothCountMap.values()){
            answer = answer  * (value + 1);
        }
        return answer - 1;
    }
}