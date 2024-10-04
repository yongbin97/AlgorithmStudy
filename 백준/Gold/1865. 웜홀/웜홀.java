import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  static class Edge {

    int u;
    int v;
    int w;

    public Edge(int u, int v, int w) {
      this.u = u;
      this.v = v;
      this.w = w;
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();

    int T = stoi(br.readLine().strip());

    for (int i = 0; i < T; i++) {
      String[] input = br.readLine().split(" ");

      int N = stoi(input[0]);
      int M = stoi(input[1]);
      int W = stoi(input[2]);

      List<Edge> edges = new ArrayList<>();

      for (int j = 0; j < M; j++) {
        input = br.readLine().split(" ");
        int u = stoi(input[0]);
        int v = stoi(input[1]);
        int w = stoi(input[2]);

        edges.add(new Edge(u, v, w));
        edges.add(new Edge(v, u, w));
      }

      for (int j = 0; j < W; j++) {
        input = br.readLine().split(" ");
        int u = stoi(input[0]);
        int v = stoi(input[1]);
        int w = stoi(input[2]);

        edges.add(new Edge(u, v, -w));
      }

      boolean flag = false;
      for (int j = 1; j <= N; j++) {
        if (bellmanFord(j, N, edges)) {
          sb.append("YES").append("\n");
          flag = true;
          break;
        }
      }
      if (!flag) {
        sb.append("NO").append("\n");
      }
    }
    System.out.println(sb.toString().strip());
  }

  private static boolean bellmanFord(int start, int N, List<Edge> edges) {
    int[] dist = new int[N + 1];
    Arrays.fill(dist, Integer.MAX_VALUE);

    dist[start] = 0;

    for (int i = 1; i <= N; i++) {
      boolean flag = false;

      for (Edge edge : edges) {
        if (dist[edge.u] == Integer.MAX_VALUE) {
          continue;
        }

        if (dist[edge.v] > dist[edge.u] + edge.w) {
          dist[edge.v] = dist[edge.u] + edge.w;
          flag = true;
          
          if (i == N) {
            return true;
          }
        }
      }
      if (!flag) {
        break;
      }
    }
    return false;
  }

  private static int stoi(String s) {
    return Integer.parseInt(s);
  }
}
