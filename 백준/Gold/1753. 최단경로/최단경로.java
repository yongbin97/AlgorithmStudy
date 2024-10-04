import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  public static int V;
  public static int E;
  public static Map<Integer, Map<Integer, Integer>> graph = new HashMap<>();
  public static int[] dist;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();

    String[] input = br.readLine().split(" ");
    V = Integer.parseInt(input[0]);
    E = Integer.parseInt(input[1]);

    int start = Integer.parseInt(br.readLine().strip());

    dist = new int[V + 1];
    Arrays.fill(dist, Integer.MAX_VALUE);

    for (int i = 1; i <= V; i++) {
      graph.put(i, new HashMap<>());
    }

    for (int i = 0; i < E; i++) {
      input = br.readLine().split(" ");
      int u = Integer.parseInt(input[0]);
      int v = Integer.parseInt(input[1]);
      int w = Integer.parseInt(input[2]);

      if (graph.get(u).getOrDefault(v, Integer.MAX_VALUE) > w) {
        graph.get(u).put(v, w);
      }
    }
    dijkstra(start);

    for (int i = 1; i <= V; i++) {
      if (dist[i] == Integer.MAX_VALUE) {
        sb.append("INF");
      } else {
        sb.append(dist[i]);
      }
      sb.append("\n");
    }

    System.out.println(sb.toString().strip());
  }

  private static void dijkstra(int start) {
    PriorityQueue<int[]> pq = new PriorityQueue<>((Comparator.comparingInt(o -> o[0])));
    dist[start] = 0;
    // dist, node
    pq.add(new int[]{0, start});

    while (!pq.isEmpty()) {
      int[] curr = pq.poll();
      int node = curr[1];
      int weight = curr[0];

      if (weight > dist[node]) continue;

      for (int next: graph.get(node).keySet()) {
        if (dist[next] >= weight + graph.get(node).get(next)) {
          dist[next] = weight + graph.get(node).get(next);
          pq.add(new int[] {dist[next], next});
        }
      }
    }
  }
}
