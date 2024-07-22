import java.util.*;


class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0; 
        
        Map<String, Map<String, Integer>> fromToCountMap = new HashMap<>();
        Map<String, Integer> giftIndexMap = new HashMap<>();
        
        // init Map
        for (String friend: friends) {
            fromToCountMap.put(friend, new HashMap<>());
            giftIndexMap.put(friend, 0);
        }
        
        // set map
        for (String gift: gifts) {
            String[] fromTo = gift.split(" ");
            
            fromToCountMap.get(fromTo[0]).putIfAbsent(fromTo[1], 0);
            fromToCountMap.get(fromTo[1]).putIfAbsent(fromTo[0], 0);
            fromToCountMap.get(fromTo[0]).put(fromTo[1], fromToCountMap.get(fromTo[0]).get(fromTo[1]) + 1);
            fromToCountMap.get(fromTo[1]).put(fromTo[0], fromToCountMap.get(fromTo[1]).get(fromTo[0]) - 1);
            
            giftIndexMap.put(fromTo[0], giftIndexMap.get(fromTo[0]) + 1);
            giftIndexMap.put(fromTo[1], giftIndexMap.get(fromTo[1]) - 1);
        }
        
        
        // get answer
        for (String fromFriend: friends) {
            int count = 0;
            Map<String, Integer> fromCountMap = fromToCountMap.get(fromFriend);
            for (String toFriend: friends) {
                if (fromFriend.equals(toFriend)) continue;
                
                if (!fromCountMap.containsKey(toFriend) || fromCountMap.get(toFriend) == 0) {
                    if (giftIndexMap.get(fromFriend) > giftIndexMap.get(toFriend)) count ++;
                } else {
                    if (fromCountMap.get(toFriend) > 0) count ++;
                }
            }
            System.out.println(fromFriend + " : " + count);
            answer = Math.max(answer, count);
        }
        
        return answer;
    }
}