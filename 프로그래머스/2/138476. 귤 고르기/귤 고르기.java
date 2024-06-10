import java.util.*;


class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
            
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int t: tangerine){
            int count = countMap.getOrDefault(t, 0) + 1;
            countMap.put(t, count);
        }
        
        List<Integer> keySet = new ArrayList<>(countMap.keySet());
        keySet.sort((o1, o2) -> countMap.get(o2).compareTo(countMap.get(o1)));
        
        for (int key: keySet){
            if (k > 0){
                k -= countMap.get(key);
                answer ++;
            } else return answer;
        }
        
        return answer;
    }
}