class Solution {
    public long solution(int k, int d) {
        long answer = 0;
        
        for (int i = 0; i * k <= d; i ++){
            double x = i * k;
            double maxY = Math.sqrt(Math.pow(d, 2) - Math.pow(x, 2));
            answer += (int) maxY / k + 1;   
        }
        return answer;
    }
}