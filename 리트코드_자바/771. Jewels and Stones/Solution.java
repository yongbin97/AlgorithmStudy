import java.util.*;


class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int answer = 0;
        Map<Character, Integer> stoneCountMap = new HashMap<>();

        for (char stone: stones.toCharArray()){
            int count = stoneCountMap.getOrDefault(stone, 0);
            stoneCountMap.put(stone, count + 1);
        }

        for (char jewel: jewels.toCharArray()){
            answer += stoneCountMap.getOrDefault(jewel, 0);
        }

        return answer;
    }
}