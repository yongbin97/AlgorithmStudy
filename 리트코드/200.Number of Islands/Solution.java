import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int numIslands(char[][] grid) {
        int answer = 0;
        int m = grid.length;
        int n = grid[0].length;

        int[][] visited = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] == 0 && grid[i][j] == '1') {
                    System.out.println("i, j = " + i + ", " + j);
                    visited = searchBFS(grid, visited, i, j);
                    answer += 1;
                }
            }
        }
        return answer;
    }

    public int[][] searchBFS(char[][] grid, int[][] visited, int r, int c) {
        int[][] dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        Queue<int[]> dq = new ArrayDeque<>();
        dq.offer(new int[]{r, c});
        visited[r][c] = 1;

        while (!dq.isEmpty()) {
            int[] curr = dq.poll();

            for (int[] dir : dirs) {
                int nx = curr[0] + dir[0];
                int ny = curr[1] + dir[1];

                if (nx < 0 || nx >= grid.length || ny < 0 || ny >= grid[0].length) continue;
                if (visited[nx][ny] == 1 || grid[nx][ny] == '0') continue;

                visited[nx][ny] = 1;
                dq.offer(new int[]{nx, ny});

            }
        }
        return visited;
    }
}