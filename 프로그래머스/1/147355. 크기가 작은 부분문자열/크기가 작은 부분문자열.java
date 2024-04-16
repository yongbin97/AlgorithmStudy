class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        Long num = Long.parseLong(p);
        
        for (int i = 0; i < t.length() - p.length() + 1; i ++){
            if (Long.parseLong(t.substring(i, i + p.length())) <= num){
                answer ++;
            }
        }
        
        return answer;
    }
}