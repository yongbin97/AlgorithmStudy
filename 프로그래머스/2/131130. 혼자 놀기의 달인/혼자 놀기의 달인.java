import java.util.*;

class Solution {
    public int solution(int[] cards) {
        int[] visited = new int[cards.length];
        List<Integer> countList = new ArrayList<>();
        
        for (int i = 0; i < cards.length; i++){
            if (visited[i] == 0){
                int count = dfs(i + 1, visited, cards);
                countList.add(count);
            }
        }
        countList.sort((o1, o2) -> o2 - o1);
        
        if (countList.size() == 1) return 0;
        else return countList.get(0) * countList.get(1);
    }
    
   public int dfs(int curr, int[] visited, int[] cards){
       int count = 1;
       
       visited[curr - 1] = 1;
       int next = cards[curr - 1];

       while (visited[next - 1] != 1){
           visited[next - 1] = 1;
           next = cards[next - 1];
           count += 1;
       }
       
       return count;
   }
}