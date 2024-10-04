import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  private static int N;
  private static int M;
  private static int[][] graph;
  private static int[][] dirs = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};


  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String[] input = br.readLine().split(" ");
    N = stoi(input[0]);
    M = stoi(input[1]);

    graph = new int[N][M];

    for (int i = 0; i < N; i++) {
      input = br.readLine().split("");
      for (int j = 0; j < M; j++) {
        graph[i][j] = stoi(input[j]);
      }
    }

    System.out.println(bfs());

  }

  private static int bfs() {
    // visited[i][j][1] = remain 1 , visited[i][j][0] = remain 0
    int[][][] visited = new int[N][M][2];

    Deque<int[]> dq = new ArrayDeque<>();
    // r, c, remain
    dq.add(new int[]{0, 0, 1});
    visited[0][0][1] = 1;

    while (!dq.isEmpty()) {
      int[] curr = dq.pollFirst();
      int r = curr[0];
      int c = curr[1];
      int remain = curr[2];

      if (r == N - 1 && c == M - 1) {
        return visited[r][c][remain];
      }

      for (int[] dir : dirs) {
        int nr = r + dir[0];
        int nc = c + dir[1];

        if (inRange(nr, nc)) {
          // 1. 벽이 없는 경우
          if (graph[nr][nc] == 0 && visited[nr][nc][remain] == 0) {
            visited[nr][nc][remain] = visited[r][c][remain] + 1;
            dq.add(new int[]{nr, nc, remain});
          }
          // 2. 벽이 있지만, 부술 수 있는 경우
          else if (graph[nr][nc] == 1 && remain == 1 && visited[nr][nc][0] == 0) {
            visited[nr][nc][0] = visited[r][c][remain] + 1;
            dq.add(new int[]{nr, nc, 0});
          }
        }
      }
    }
    return -1;
  }


  private static boolean inRange(int x, int y) {
    return 0 <= x && x < N && 0 <= y && y < M;
  }

  private static int stoi(String s) {
    return Integer.parseInt(s);
  }
}
