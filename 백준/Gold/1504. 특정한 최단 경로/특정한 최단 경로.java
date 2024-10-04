import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  private static int N;
  private static int E;
  private static Map<Integer, Map<Integer, Integer>> graph = new HashMap<>();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String[] input = br.readLine().split(" ");
    N = Integer.parseInt(input[0]);
    E = Integer.parseInt(input[1]);

    for (int i = 1; i <= N; i++) {
      graph.put(i, new HashMap<>());
    }

    for (int i = 0; i < E; i++) {
      input = br.readLine().split(" ");
      int u = Integer.parseInt(input[0]);
      int v = Integer.parseInt(input[1]);
      int w = Integer.parseInt(input[2]);

      graph.get(u).put(v, w);
      graph.get(v).put(u, w);
    }

    input = br.readLine().split(" ");
    int v1 = Integer.parseInt(input[0]);
    int v2 = Integer.parseInt(input[1]);

    int[] dist1 = dijkstra(1);
    int[] distV1 = dijkstra(v1);
    int[] distV2 = dijkstra(v2);

    int answer1 =
        dist1[v1] == Integer.MAX_VALUE || distV1[v2] == Integer.MAX_VALUE || distV2[N] == Integer.MAX_VALUE ?
        Integer.MAX_VALUE : dist1[v1] + distV1[v2] + distV2[N];

    int answer2 =
        dist1[v2] == Integer.MAX_VALUE || distV2[v1] == Integer.MAX_VALUE || distV1[N] == Integer.MAX_VALUE ?
            Integer.MAX_VALUE : dist1[v2] + distV2[v1] + distV1[N];

    int answer = Math.min(answer1, answer2);
    if (answer == Integer.MAX_VALUE){
      System.out.println(-1);
    } else {
      System.out.println(answer);
    }
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
