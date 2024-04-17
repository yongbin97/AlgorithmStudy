class Solution {
    public int solution(String s) {
        int answer = 0;
        
        char first = s.charAt(0);
        int count = 0;
        
        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == first){
                count ++;
            } else{
                count --;
            }
            if (count == 0){
                answer ++;
                if (i < s.length() - 1){
                    first = s.charAt(i + 1);
                }
            }            
        }
        if (count != 0){
            answer ++;
        }
        
        return answer;
    }
}