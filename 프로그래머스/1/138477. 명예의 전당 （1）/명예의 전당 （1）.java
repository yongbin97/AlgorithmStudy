import java.util.*;


class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        List<Integer> topK = new ArrayList<>(3);
        
        for (int i = 0; i < score.length; i ++){
            int s = score[i];
            
            if (topK.size() < k){
                topK.add(s);
            } else if (topK.get(topK.size() -1) < s){
                topK.set(topK.size()-1, s);
            }
            Collections.sort(topK, Collections.reverseOrder());
            answer[i] = topK.get(topK.size() - 1);
        }
        
        return answer;
    }
}