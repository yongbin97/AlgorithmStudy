class Solution {
    public long solution(int r1, int r2) {
        long answer = 0L;
        
        for (int i = 0; i < r1; i++){
            answer += (long) Math.floor(Math.sqrt((long)r2 * r2 - (long) i * i)) - Math.ceil(Math.sqrt((long)r1 * r1 - (long) i * i)) + 1L;
        }
        for (int i = r1; i < r2; i++){
            answer += (long) Math.floor(Math.sqrt((long) r2 * r2 - (long) i * i));
        }
        
        return answer * 4L;
    }
}