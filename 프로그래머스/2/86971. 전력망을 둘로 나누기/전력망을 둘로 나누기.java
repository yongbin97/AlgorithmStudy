import java.util.*;

class Solution {
    int answer = Integer.MAX_VALUE;
    
    public int solution(int n, int[][] wires) {
        for (int i = 0; i < wires.length; i++) {
            search(n, i, wires);   
        }
        return answer;
    }
    
    public void search(int n, int idx, int[][] wires) {
        Map<Integer, List<Integer>> wireMap = new HashMap<>();
        
        for (int i = 1; i < n + 1; i++) {
            wireMap.put(i, new ArrayList<>());
        }
        
        
        for (int i = 0; i < wires.length; i++) {
            if (i == idx) continue;
            
            wireMap.get(wires[i][0]).add(wires[i][1]);
            wireMap.get(wires[i][1]).add(wires[i][0]);
        }
        int cnt = getNodeCount(n, wireMap);
        answer = Math.min(answer, Math.abs(n - 2 * cnt));
    }
    
    public int getNodeCount(int n, Map<Integer, List<Integer>> wireMap) {
        int count = 0;
        int[] visited = new int[n + 1];
        
        Deque<Integer> dq = new ArrayDeque<>();
        dq.add(1);
        visited[1] = 1;
        
        while (!dq.isEmpty()) {
            int curr = dq.poll();
            count ++;
            
            if (wireMap.get(curr).size() == 0) continue;
            for (int next: wireMap.get(curr)) {
                if (visited[next] == 0) {
                    visited[next] = 1;
                    dq.add(next);
                }
            }
        }
        return count;
    }
}