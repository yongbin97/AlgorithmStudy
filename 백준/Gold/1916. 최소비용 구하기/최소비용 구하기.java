import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  private static int N;
  private static int M;
  private static int[] dist;
  private static Map<Integer, Map<Integer, Integer>> graph = new HashMap<>();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    N = Integer.parseInt(br.readLine().strip());
    M = Integer.parseInt(br.readLine().strip());

    for (int i = 1; i <= N; i++) {
      graph.put(i, new HashMap<>());
    }
    dist = new int[N + 1];
    Arrays.fill(dist, Integer.MAX_VALUE);

    String[] input;

    for (int i = 0; i < M; i++) {
      input = br.readLine().split(" ");
      int u = Integer.parseInt(input[0]);
      int v = Integer.parseInt(input[1]);
      int w = Integer.parseInt(input[2]);

      if (graph.get(u).getOrDefault(v, Integer.MAX_VALUE) > w){
        graph.get(u).put(v, w);
      }
    }

    input = br.readLine().split(" ");
    int start = Integer.parseInt(input[0]);
    int end = Integer.parseInt(input[1]);
    dijkstra(start);
    System.out.println(dist[end]);
  }

  private static void dijkstra(int start) {
    PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));
    dist[start] = 0;

    pq.add(new int[]{start, 0});

    while (!pq.isEmpty()) {
      int[] curr = pq.poll();
      int node = curr[0];
      int d = curr[1];

      if (d > dist[node]) continue;

      for (int next: graph.get(node).keySet()) {
        if (dist[next] > graph.get(node).get(next) + d) {
          dist[next] = graph.get(node).get(next) + d;
          pq.add(new int[] {next, dist[next]});
        }
      }
    }
  }
}
