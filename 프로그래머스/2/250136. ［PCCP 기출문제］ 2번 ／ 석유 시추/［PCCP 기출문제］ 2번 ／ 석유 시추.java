import java.util.*;

class Solution {
    public int solution(int[][] land) {
        int answer = 0;
        int groupIdx = 1;
        Map<Integer, Integer> groupIdxCountMap = new HashMap<>();
        int[][] visited = new int[land.length][land[0].length];
        
        for (int col = 0; col < land[0].length; col++){
            int colCount = 0;
            Set<Integer> groupSet = new HashSet<>();
            for (int row = 0; row < land.length; row++){
                if (land[row][col] != 0){
                    if (visited[row][col] == 0){
                        groupIdxCountMap.put(groupIdx, search(groupIdx, row, col, land, visited));
                        groupIdx ++;
                    }
                    
                    if (!groupSet.contains(visited[row][col])){
                        groupSet.add(visited[row][col]);
                        colCount += groupIdxCountMap.get(visited[row][col]);
                    }
                }
            }
            answer = Math.max(answer, colCount);
        }
        
        return answer;
    }
    
    public int search(int groupIdx, int r, int c, int[][] land, int[][] visited){
        int count = 1;
        int[][] dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {r, c});
        visited[r][c] = groupIdx;
        
        while (!queue.isEmpty()){
            int[] curr = queue.poll();

            for (int[] dir: dirs){
                int nextR = curr[0] + dir[0];
                int nextC = curr[1] + dir[1];
                
                if (nextR < 0 || nextR >= land.length 
                    || nextC < 0 || nextC >= land[0].length) 
                    continue;
                if (
                    land[nextR][nextC] != 0
                    && visited[nextR][nextC] == 0
                   ){
                    queue.offer(new int[] {nextR, nextC});
                    visited[nextR][nextC] = groupIdx;
                    count += 1;
                }
            }
        }
        
        return count;
    }
}