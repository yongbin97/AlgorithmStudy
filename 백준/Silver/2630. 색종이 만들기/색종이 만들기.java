import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

  private static int N;
  private static int[][] graph;
  private static int[] answer = new int[2];

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    N = Integer.parseInt(br.readLine().strip());
    graph = new int[N][N];

    for (int i = 0; i < N; i++) {
      String[] row = br.readLine().split(" ");

      for (int j = 0; j < N; j++) {
        graph[i][j] = Integer.parseInt(row[j]);
      }
    }
    solution();

    for (int count : answer) {
      System.out.println(count);
    }

    br.close();
  }

  private static void solution() {
    boolean[][] visited = new boolean[N][N];

    int len = N;

    while (len >= 1) {
      for (int i = 0; i < N; i += len) {
        for (int j = 0; j < N; j += len) {
          if (!visited[i][j]) {
            isSameColor(i, j, len, visited);
          }
        }
      }
      len /= 2;
    }
  }

  private static void isSameColor(int r, int c, int len, boolean[][] visited) {
    int target = graph[r][c];

    for (int i = r; i < r + len; i++) {
      for (int j = c; j < c + len; j++) {
        if (graph[i][j] != target) {
          return;
        }
      }
    }

    for (int i = r; i < r + len; i++) {
      for (int j = c; j < c + len; j++) {
        visited[i][j] = true;
      }
    }
    answer[target] += 1;
  }
}