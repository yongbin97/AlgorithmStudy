import java.util.*;


class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        Map<Character, Integer> charIdxMap = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            int idx = charIdxMap.getOrDefault(c, i + 1);
            
            answer[i] = i - idx;
            charIdxMap.put(c, i);
        }
        
        return answer;
    }
}