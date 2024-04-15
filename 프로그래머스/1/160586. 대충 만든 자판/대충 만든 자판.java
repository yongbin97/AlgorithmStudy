import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        Map<Character, Integer> keyCountMap = new HashMap<>();
        
        for (String key: keymap){
            for (int i=0; i < key.length(); i++){
                int count = Math.min(keyCountMap.getOrDefault(key.charAt(i), 100), i + 1);
                keyCountMap.put(key.charAt(i), count);
            }
        }
        
        for (int i = 0; i < targets.length; i++){
            int count = 0;
            for (char c: targets[i].toCharArray()){
                if (keyCountMap.containsKey(c)){
                    count += keyCountMap.get(c);                
                } else {
                    count = -1;
                    break;
                }
            }
            answer[i] = count;
        }
        
        return answer;
    }
}