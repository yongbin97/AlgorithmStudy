import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> countMap = new HashMap<>();
        for (String p: participant){
            countMap.put(p, countMap.getOrDefault(p, 0) + 1);
        }
        
        for (String c: completion){
            int count = countMap.get(c);
            if (count == 1){
                countMap.remove(c);
            } else {
                countMap.put(c, count - 1);
            }
        }
        String answer = "";
        for (String key: countMap.keySet()){
            answer = key;
        }
        return answer;
    }
}