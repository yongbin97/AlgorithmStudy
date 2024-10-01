import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  public static int N;
  public static int M;
  public static int[][] edges;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String[] row = br.readLine().split(" ");
    N = Integer.parseInt(row[0]);
    M = Integer.parseInt(row[1]);

    edges = new int[N + 1][N + 1];

    for (int i = 0; i < M; i++) {
      row = br.readLine().split(" ");
      int u = Integer.parseInt(row[0]);
      int v = Integer.parseInt(row[1]);

      edges[u][v] = 1;
      edges[v][u] = 1;
    }

    System.out.println(search());
  }

  private static int search() {
    boolean[] visited = new boolean[N + 1];

    int cnt = 0;

    for (int i = 1; i <= N; i++) {
      if (!visited[i]) {
        visited[i] = true;
        bfs(i, visited);
        cnt ++;
      }
    }

    return cnt;
  }

  private static void bfs(int node, boolean[] visited) {
    Deque<Integer> dq = new ArrayDeque<>();
    dq.add(node);

    while (!dq.isEmpty()) {
      int curr = dq.pollFirst();

      for (int i = 1; i <= N; i++) {
        if (edges[curr][i]== 1 && !visited[i]) {
          dq.add(i);
          visited[i] = true;
        }
      }
    }
  }
}