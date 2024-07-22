import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < friends.length; i++){
            map.put(friends[i], i);
        }
        
        int[] index = new int[friends.length];
        int[][] record = new int[friends.length][friends.length];
        
        for (String gift: gifts) {
            String[] curr = gift.split(" ");
            
            index[map.get(curr[0])] ++;
            index[map.get(curr[1])] --;
            record[map.get(curr[0])][map.get(curr[1])] ++;
        }
        
        for (int i = 0; i < friends.length; i++) {
            int cnt = 0;
            for (int j = 0; j < friends.length; j++) {
                if (i == j) continue;
                if (record[i][j] > record[j][i]) cnt ++;
                else if (record[i][j] == record[j][i] && index[i] > index[j]) cnt ++;
            }
            answer = Math.max(answer, cnt);
        }
        
        return answer;
    }
}