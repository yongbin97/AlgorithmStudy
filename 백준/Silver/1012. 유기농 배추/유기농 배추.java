import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

  public static int[][] dirs = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();

    int T = Integer.parseInt(br.readLine().strip());

    for (int i = 0; i < T; i++) {
      String[] row = br.readLine().split(" ");
      int M = Integer.parseInt(row[0]);
      int N = Integer.parseInt(row[1]);
      int K = Integer.parseInt(row[2]);

      int[][] graph = new int[M][N];
      for (int j = 0; j < K; j++) {
        row = br.readLine().split(" ");
        int x = Integer.parseInt(row[0]);
        int y = Integer.parseInt(row[1]);

        graph[x][y] = 1;
      }

      sb.append(solution(M, N, graph)).append("\n");
    }

    System.out.println(sb.toString().strip());

    br.close();
  }

  private static int solution(int M, int N, int[][] graph) {
    int count = 0;

    boolean[][] visited = new boolean[M][N];

    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        if (!visited[i][j] && graph[i][j] == 1) {
          visited[i][j] = true;
          bfs(i, j, visited, graph);
          count++;
        }
      }
    }

    return count;
  }

  private static void bfs(int r, int c, boolean[][] visited, int[][] graph) {
    Deque<int[]> dq = new ArrayDeque<>();
    dq.add(new int[]{r, c});

    while (!dq.isEmpty()) {
      int[] curr = dq.pollFirst();

      for (int[] dir : dirs) {
        int nr = curr[0] + dir[0];
        int nc = curr[1] + dir[1];

        if (inRange(nr, nc, graph.length, graph[0].length) && !visited[nr][nc] && graph[nr][nc] == 1){
          visited[nr][nc] = true;
          dq.add(new int[]{nr, nc});
        }
      }
    }
  }

  private static boolean inRange(int x, int y, int maxX, int maxY) {
    return 0 <= x && x < maxX && 0 <= y && y < maxY;
  }
}