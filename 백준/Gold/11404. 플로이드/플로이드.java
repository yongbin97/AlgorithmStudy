import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  public static int n;
  public static Map<Integer, Map<Integer, Integer>> graph = new HashMap<>();


  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();

    n = Integer.parseInt(br.readLine().strip());
    int m = Integer.parseInt(br.readLine().strip());

    for (int i = 1; i <= n; i++) {
      graph.put(i, new HashMap<>());
    }

    for (int i = 0; i < m; i++) {
      String[] input = br.readLine().split(" ");
      int a = Integer.parseInt(input[0]);
      int b = Integer.parseInt(input[1]);
      int c = Integer.parseInt(input[2]);

      if (graph.get(a).getOrDefault(b, Integer.MAX_VALUE) > c) {
        graph.get(a).put(b, c);
      }
    }

    for (int i = 1; i <= n; i++) {
      int[] dist = dijkstra(i);

      for (int j = 1; j <= n; j++) {
        if (dist[j] == Integer.MAX_VALUE) {
          sb.append(0).append(" ");
        } else {
          sb.append(dist[j]).append(" ");
        }
      }
      sb.append("\n");
    }

    System.out.println(sb.toString().strip());
  }

  private static int[] dijkstra(int start) {
    int[] dist = new int[n + 1];
    Arrays.fill(dist, Integer.MAX_VALUE);

    PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));
    // node, dist
    pq.add(new int[]{start, 0});
    dist[start] = 0;

    while (!pq.isEmpty()) {
      int[] curr = pq.poll();
      int node = curr[0];
      int d = curr[1];

      if (d > dist[node]) {
        continue;
      }

      for (int next : graph.get(node).keySet()) {
        if (dist[next] > graph.get(node).get(next) + d) {
          dist[next] = graph.get(node).get(next) + d;
          pq.add(new int[]{next, dist[next]});
        }
      }
    }

    return dist;
  }
}
