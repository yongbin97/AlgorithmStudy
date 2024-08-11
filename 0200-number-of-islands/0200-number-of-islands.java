import java.util.*;

class Solution {
    int[][] dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    public void bfs(int r, int c, char[][] grid, boolean[][] visited) {
        Queue<int[]> queue = new ArrayDeque<>();

        queue.add(new int[]{r, c});
        visited[r][c] = true;

        while(!queue.isEmpty()) {
            int[] curr = queue.poll();

            for (int[] dir: dirs) {
                int nextR = curr[0] + dir[0];
                int nextC = curr[1] + dir[1];

                if (nextR < 0 || nextR >= grid.length || nextC < 0 || nextC >= grid[0].length) continue;
                if (grid[nextR][nextC] == '0' || visited[nextR][nextC]) continue;

                queue.add(new int[]{nextR, nextC});
                visited[nextR][nextC] = true;
            }
        }
    }

    public int numIslands(char[][] grid) {
        int cnt = 0;
        boolean[][] visited = new boolean[grid.length][grid[0].length];

        // step 1. find '1' + not visited
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                // step 2. bfs
                if (grid[i][j] == '1' && !visited[i][j]){
                    bfs(i, j, grid, visited);
                    cnt ++;
                }
            }
        }
        
        return cnt;
    }
}