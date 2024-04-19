import java.util.*;


class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        
        for (int i = 1; i < number + 1; i++){
            int count = getCount(i);
            if (count > limit) answer += power;
            else answer += count;
        }
        
        return answer;
    }
    
    public int getCount(int number){
        if (number == 1) return 1;
        
        int count = 0;
        for (int i = 1; i * i <= number; i ++){
            if (i * i == number){
                count += 1;
            } else if (number % i == 0){
                count += 2;
            }
        }
        return count;
    }
}