class Solution {
    public int solution(int storey) {
        int answer = 0;

        while (storey > 0){
            if (storey % 10 == 5 && storey % 100 < 50){
                answer += 5;
                storey /= 10;
            } else {
                answer += Math.min(10 - (storey % 10), storey % 10);
                storey = (int) Math.round(storey / 10.0);
            }
        }
        return answer;
    }
}