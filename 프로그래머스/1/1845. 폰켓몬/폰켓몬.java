import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        Map<Integer, Integer> countMap = new HashMap<>();
        
        for (int num: nums){
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }
        
        return Math.min(countMap.keySet().size(), (int) nums.length / 2);
    }
}