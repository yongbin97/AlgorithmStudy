import java.util.*;

class Solution {
    int w, h;
    char[][] graph;
    int[][][] visited;
    int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    
    public void setGraph(String[] grid) {
        w = grid[0].length();
        h = grid.length;
        
        graph = new char[h][w];
        for (int i = 0; i < h; i++) {
            graph[i] = grid[i].toCharArray();
        }
        visited = new int[h][w][4];
    }
    
    public int move(int x, int y, int dirIdx) {
        int count = 0;
        
        Deque<int[]> dq = new ArrayDeque<>();
        dq.add(new int[] {x, y, dirIdx});
        
        while (!dq.isEmpty()) {
            int[] curr = dq.poll();
            count ++;
            
            int nextDirIdx = getNextDirIdx(curr[2], graph[curr[0]][curr[1]]);
            int nextX = (curr[0] + directions[nextDirIdx][0] + h) % h;
            int nextY = (curr[1] + directions[nextDirIdx][1] + w) % w;
            
            if (visited[nextX][nextY][nextDirIdx] == 0) {
                visited[nextX][nextY][nextDirIdx] = 1;
                dq.add(new int[]{nextX, nextY, nextDirIdx});
            }
        }
        return count;
    }
    
    public int getNextDirIdx(int dirIdx, char node) {
        if (node == 'S') return dirIdx;
        else if (node == 'L') return (dirIdx + 5) % 4;
        else return (dirIdx + 3) % 4;
    }
    
    public int[] solution(String[] grid) {
        List<Integer> answer = new ArrayList<>();
        setGraph(grid);
        
        for(int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                for (int k = 0; k < 4; k++) {
                    if (visited[i][j][k] == 0) {
                        visited[i][j][k] = 1;
                        answer.add(move(i, j ,k));
                    }
                }
            }
        }
        return answer.stream()
            .sorted()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}