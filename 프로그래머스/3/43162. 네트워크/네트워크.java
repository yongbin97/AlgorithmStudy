import java.util.*;


class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int[] visited = new int[n];
        
        for (int i = 0; i < n; i++){
            // System.out.println("start: " + i);
            Queue<Integer> dq = new LinkedList<>();
            
            if (visited[i] == 0){
                dq.offer(i);
                visited[i] = 1;
            
                while (!dq.isEmpty()){
                    int curr = dq.poll();
                    // System.out.println("curr: " + curr);

                    for (int j = 0; j < n; j++){
                        if(visited[j] == 0 && computers[curr][j] == 1){
                            dq.offer(j);
                            visited[j] = 1;
                        }
                    }
                }
                answer ++;
            }
        }
        
        return answer;
    }
}