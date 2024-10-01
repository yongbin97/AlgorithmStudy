import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  public static int n;
  public static int m;
  public static int[] start;
  public static int[][] graph;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();

    String[] row = br.readLine().split(" ");
    n = Integer.parseInt(row[0]);
    m = Integer.parseInt(row[1]);

    graph = new int[n][m];

    for (int i = 0; i < n; i++) {
      row = br.readLine().split(" ");
      for (int j = 0; j < m; j++) {
        graph[i][j] = Integer.parseInt(row[j]);

        if (Integer.parseInt(row[j]) == 2) {
          start = new int[]{i, j};
        }
      }
    }
    int[][] maps = solution();

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (graph[i][j] == 1 && maps[i][j] == 0) {
          sb.append("-1 ");
        } else {
          sb.append(maps[i][j]).append(" ");
        }
      }
      sb.append("\n");
    }

    System.out.println(sb.toString().strip());
    br.close();
  }

  public static int[][] solution() {
    int[][] maps = new int[n][m];
    boolean[][] visited = new boolean[n][m];

    int[][] dirs = new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    Deque<int[]> dq = new ArrayDeque<>();
    dq.add(new int[]{start[0], start[1]});
    visited[start[0]][start[1]] = true;

    while (!dq.isEmpty()) {
      int[] curr = dq.pollFirst();

      for (int[] dir : dirs) {
        int nr = curr[0] + dir[0];
        int nc = curr[1] + dir[1];

        if (inRange(nr, nc) && graph[nr][nc] == 1 && !visited[nr][nc]) {
          maps[nr][nc] = maps[curr[0]][curr[1]] + 1;
          visited[nr][nc] = true;
          dq.add(new int[]{nr, nc});
        }
      }
    }
    return maps;
}

  public static boolean inRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
  }
}
