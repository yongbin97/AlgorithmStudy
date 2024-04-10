import java.util.*;


class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> rankMap = new HashMap<>();
        
        for (int i=0; i < players.length; i++){
            rankMap.put(players[i], i);
        }
        
        for (String player: callings){
            int rank = rankMap.get(player);
            String frontPlayer = players[rank - 1];
            
            rankMap.replace(player, rank - 1);
            rankMap.replace(frontPlayer, rank);
            
            players[rank-1] = player;
            players[rank] = frontPlayer;
        }
        
        return players;
    }
}