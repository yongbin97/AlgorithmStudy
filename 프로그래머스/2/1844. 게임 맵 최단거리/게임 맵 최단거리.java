import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;

        int[][] visited = new int[n][m];

        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0});
        visited[0][0] = 1;

        while (!q.isEmpty()) {
            int[] curr = q.poll();

            for (int[] dir : dirs) {
                int nx = curr[0] + dir[0];
                int ny = curr[1] + dir[1];

                // map 밖인지 확인
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

                // 벽인지 확인
                if (maps[nx][ny] == 0) continue;

                // 이동
                if (maps[nx][ny] == 1 && visited[nx][ny] == 0) {
                    visited[nx][ny] = visited[curr[0]][curr[1]] + 1;
                    q.add(new int[]{nx, ny});
                }

            }
        }


        if (visited[n - 1][m - 1] == 0) {
            return -1;
        } else {
            return visited[n - 1][m - 1];
        }
    }
}