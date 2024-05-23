import java.util.List;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;


class Solution {
    public int solution(int x, int y, int n) {
        int[] visited = new int[y + 1];
        
        if (x == y) return 0;
        
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {x, 0});
        visited[x] = 1;
        
        while (!q.isEmpty()){
            int[] curr = q.poll();
            int num = curr[0];
            int idx = curr[1];
            
            List<Integer> nextNums = getNonVisited(visited, num, y, n);
            
            for (Integer next: nextNums){
                if (next == y) return idx + 1;
                visited[next] = 1;
                if (next < y) q.add(new int[] {next, idx + 1});
            }          
        }
        return -1;
    }
    
    private List<Integer> getNonVisited(int[] visited, int num, int target, int n){
        List<Integer> numList = new ArrayList<>();
        
        if (target >= num * 2 && visited[num * 2] == 0) numList.add(num * 2);
        if (target >= num * 3 && visited[num * 3] == 0) numList.add(num * 3);
        if (target >= num + n && visited[num + n] == 0) numList.add(num + n);
        
        return numList;
    }
}