import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  private static int N;
  private static Map<Integer, Map<Integer, Integer>> graph = new HashMap<>();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String[] input = br.readLine().split(" ");
    N = Integer.parseInt(input[0]);
    int M = Integer.parseInt(input[1]);
    int X = Integer.parseInt(input[2]);

    for (int i = 1; i <= N; i++) {
      graph.put(i, new HashMap<>());
    }

    for (int i = 0; i < M; i++) {
      input = br.readLine().split(" ");
      int u = Integer.parseInt(input[0]);
      int v = Integer.parseInt(input[1]);
      int w = Integer.parseInt(input[2]);

      graph.get(u).put(v, w);
    }

    int answer = 0;
    int[] dist = dijkstra(X);

    for (int i = 1; i <= N; i++) {
      if (i == X) continue;
      int curr = dijkstra(i)[X] + dist[i];
      answer = Math.max(answer, curr);
    }

    System.out.println(answer);

  }

  private static int[] dijkstra(int start) {
    int[] dist = new int[N + 1];
    Arrays.fill(dist, Integer.MAX_VALUE);

    PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));
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
