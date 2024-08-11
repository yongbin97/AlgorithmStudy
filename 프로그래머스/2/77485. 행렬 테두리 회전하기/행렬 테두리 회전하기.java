import java.util.*;

class Solution {
    public void printGraph(int[][] graph) {
        for (int i = 0; i < graph.length; i++) {
            System.out.println(Arrays.toString(graph[i]));
        }
    }
    
    public int rotate(int[][] graph, int[] query) {
        int x1 = query[0] - 1;
        int y1 = query[1] - 1;
        int x2 = query[2] - 1;
        int y2 = query[3] - 1;
        int tmp = graph[x1][y2];
        
        int min = tmp;
        
        // (x1, y1) ~ (x1, y2 - 1) => 1칸 오른쪽
        for (int dy = y2; dy > y1; dy--) {
            min = Math.min(min, graph[x1][dy-1]);
            graph[x1][dy] = graph[x1][dy - 1];
        }
        // (x2, y1) ~ (x1 + 1, y1) => 1칸 위로
        for (int dx = x1; dx < x2; dx ++) {
            min = Math.min(min, graph[dx + 1][y1]);
            graph[dx][y1] = graph[dx + 1][y1];
        }
        
        // (x2, y2) ~ (x2, y1 + 1) => 1칸 왼쪽
        for (int dy = y1; dy < y2; dy++) {
            min = Math.min(min, graph[x2][dy + 1]);
            graph[x2][dy] = graph[x2][dy + 1];
        }
        
        //(x1, y2) ~ (x2 - 1, y2) => 1칸 아래
        for (int dx = x2; dx > x1; dx--) {
            min = Math.min(min, graph[dx - 1][y2]);
            graph[dx][y2] = graph[dx - 1][y2];
        }
        
        graph[x1 + 1][y2] = tmp;
        
        return min;
    }
    
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        
        int[][] graph = new int[rows][columns];
        int idx = 1;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                graph[i][j] = idx;
                idx ++;
            }
        }
        
        for (int i = 0; i < queries.length; i++) {
            int min = rotate(graph, queries[i]);
            answer[i] = min;
            
        }
        
        return answer;
    }
}