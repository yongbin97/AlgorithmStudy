import java.util.*;


class Solution {
    public String solution(String s, String skip, int index) {
        String answer = "";
        Integer[] skipArr = new Integer[skip.length()];
        
        for (int i = 0; i < skip.length(); i++){
            skipArr[i] = skip.charAt(i) - 0;
        }
        
        for (char c: s.toCharArray()){
            int newC = c - 0;
            for (int i = 0; i < index; i++){
                do {
                    newC = (newC - 96) % 26 + 97;    
                }
                while (Arrays.asList(skipArr).contains(newC));
            }
            answer += (char) newC;
        }
        
        return answer;
    }
}