import java.util.List;
import java.util.Queue;
import java.util.ArrayList;
import java.util.LinkedList;

class Solution {
    public int[] solution(String[] maps) {
        List<Integer> result = new ArrayList<>();
        
        char[][] grid = new char[maps.length][maps[0].length()];
        int[][] visited = new int[maps.length][maps[0].length()];
        
        for (int i = 0; i < maps.length; i++) {
            grid[i] = maps[i].toCharArray();
        }
        
        for (int x = 0; x < maps.length; x++){
            for (int y = 0; y < maps[0].length(); y++){
                if (grid[x][y] != 'X' && visited[x][y] == 0){
                    result.add(BFS(x, y, grid, visited));
                }
            }
        }
       
        if (result.size() > 0){
            return result.stream()
                .mapToInt(Integer::intValue)
                .sorted()
                .toArray();
        } else {
            return new int[] {-1};
        }

    }
    
    public int BFS(int x, int y, char[][] grid, int[][] visited){
        int total = grid[x][y] -'0';
        
        Queue<int[]> dq = new LinkedList<>();
        visited[x][y] = 1;
        dq.offer(new int[] {x, y});

        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        while(!dq.isEmpty()){
            int[] curr = dq.poll();
            
            for (int[] dir: dirs){
                int nextX = curr[0] + dir[0];
                int nextY = curr[1] + dir[1];
                
                if (nextX < 0 || nextX >= grid.length || nextY < 0 || nextY >= grid[0].length) continue;
                
                if (grid[nextX][nextY] == 'X') continue;
                
                if (visited[nextX][nextY] == 0){
                    total += grid[nextX][nextY] - '0';
                    dq.offer(new int[] {nextX, nextY});
                    visited[nextX][nextY] = 1;
                }
            }
        }
        return total;
    }
}