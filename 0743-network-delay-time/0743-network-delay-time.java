import java.util.*;

class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        /**
         * [문제]
         * times = [[from, to, time]]
         * k번 노드에서 시작해서 n개의 노드에 모두 탐색하는데 걸리는 최소 시간
         * 불가능하면 return -1
         *
         * [풀이]
         * k번 노드부터 시작하여 BFS 탐색.
         * timeOfNodes = int[] -> timeOfNodes[i] = i번 노드의 최소 탐색 시간
         */
        // timeOfNodes[i]: i번 노드의 최소 탐색 시간 (0번 idx 무시)
        int[] timeOfNodes = new int[n + 1];
        Arrays.fill(timeOfNodes, -1);
        // {from: [[to, time]]}
        Map<Integer, List<List<Integer>>> fromToNodesMap = new HashMap<>();

        // set fromToNodesMap
        for (int[] time : times) {
            List<List<Integer>> nodeList = fromToNodesMap.getOrDefault(time[0], new ArrayList<>());
            nodeList.add(List.of(time[1], time[2]));
            fromToNodesMap.put(time[0], nodeList);
        }

        // 탐색
        Queue<Integer> nodeList = new LinkedList<>();
        nodeList.add(k);
        timeOfNodes[k] = 0;

        while (!nodeList.isEmpty()) {
            int currNodeIdx = nodeList.poll();
            int currNodeTime = timeOfNodes[currNodeIdx];

            if (!fromToNodesMap.containsKey(currNodeIdx)) continue;

            for (List<Integer> next : fromToNodesMap.get(currNodeIdx)) {
                int nextNodeIdx = next.get(0);
                int currToNextTime = next.get(1);
                int nextNodeTime = timeOfNodes[nextNodeIdx];

                // 1. 다음노드 최초 방문
                // 2. 현재 노드 최소 시간 + 다음 노드 이동 시간 < 다음 노드의 최소 시간 
                //  => 갱신
                if (nextNodeTime == -1 || currNodeTime + currToNextTime < nextNodeTime) {
                    timeOfNodes[nextNodeIdx] = currNodeTime + currToNextTime;
                    nodeList.add(nextNodeIdx);
                }
            }
        }

        int answer = 0;
        for (int i = 1; i < n + 1; i++) {
            if (timeOfNodes[i] == -1) return -1;
            answer = Math.max(answer, timeOfNodes[i]);
        }

        return answer;
    }
}