import java.util.*;

class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        // timeOfNodes[i]: i번 노드의 최소 탐색 시간 (0번 idx 무시)
        int[] timeOfNodes = new int[n + 1];
        Arrays.fill(timeOfNodes, Integer.MAX_VALUE);
        // {from: [[to, time]]}
        Map<Integer, List<List<Integer>>> fromToNodesMap = new HashMap<>();

        // set fromToNodesMap
        for (int[] time : times) {
            List<List<Integer>> nodeList = fromToNodesMap.getOrDefault(time[0], new ArrayList<>());
            nodeList.add(List.of(time[1], time[2]));
            fromToNodesMap.put(time[0], nodeList);
        }

        // 탐색
        PriorityQueue<int[]> nodeList = new PriorityQueue<>(((o1, o2) -> (o1[1] - o2[1])));
        nodeList.add(new int[] {k, 0});
        timeOfNodes[k] = 0;

        while (!nodeList.isEmpty()) {
            // [nodeIdx, nodeTime]
            int[] currNode = nodeList.poll();

            if (!fromToNodesMap.containsKey(currNode[0])) continue;

            for (List<Integer> next : fromToNodesMap.get(currNode[0])) {
                int nextNodeIdx = next.get(0);
                int nextTime = currNode[1] + next.get(1);

                if (timeOfNodes[nextNodeIdx] > nextTime) {
                    timeOfNodes[nextNodeIdx] = nextTime;
                    nodeList.add(new int[] {nextNodeIdx, nextTime});
                }
            }
        }

        System.out.println(Arrays.toString(timeOfNodes));

        int answer = 0;
        for (int i = 1; i < n + 1; i++) {
            if (timeOfNodes[i] == Integer.MAX_VALUE) return -1;
            answer = Math.max(answer, timeOfNodes[i]);
        }

        return answer;
    }
}