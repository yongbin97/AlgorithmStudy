import java.util.*;

class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        /**
         * src부터 dst까지 최대 k개의 노드만 통과하여 도달할 때 최소한의 price 구하기
         */

        int[][] dist = new int[k + 1][n];
        for (int i = 0; i < k + 1; i++){
            Arrays.fill(dist[i], Integer.MAX_VALUE);
        }

        Map<Integer, Map<Integer, Integer>> graph = new HashMap<>();
        for (int[] flight : flights) {
            Map<Integer, Integer> priceMap = graph.getOrDefault(flight[0], new HashMap<>());
            priceMap.put(flight[1], flight[2]);
            graph.put(flight[0], priceMap);
        }

        // {idx, cost, k}
        dist[k][src] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> (o1[1] - o2[1]));
        pq.add(new int[]{src, 0, k});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            if (!graph.containsKey(curr[0])) continue;

            for (Map.Entry<Integer, Integer> next : graph.get(curr[0]).entrySet()) {
                int nextCost = curr[1] + next.getValue();
                if (dist[curr[2]][next.getKey()] > nextCost) {
                    dist[curr[2]][next.getKey()] = nextCost;
                    if (curr[2] > 0) pq.add(new int[]{next.getKey(), nextCost, curr[2] - 1});
                }
            }
        }
        int answer = Integer.MAX_VALUE;
        for (int i = 0; i < k + 1; i++){
            answer = Math.min(dist[i][dst], answer);
        }
        return answer != Integer.MAX_VALUE ? answer : -1;
    }
}