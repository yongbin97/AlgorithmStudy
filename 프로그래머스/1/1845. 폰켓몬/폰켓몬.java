import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int pick = nums.length / 2;
        
        Map<Integer, Integer> monsterMap = new HashMap<>();
        
        for (int num: nums) {
            monsterMap.put(num, monsterMap.getOrDefault(num, 0) + 1);
        }
        
        return Math.min(pick, monsterMap.keySet().size());
    }
}