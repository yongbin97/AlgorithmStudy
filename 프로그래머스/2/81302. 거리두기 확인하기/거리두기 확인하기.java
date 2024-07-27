import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    int[][] dir = new int[][]{{0, 1}, {1, 0}};

    public boolean search(int x, int y, char[][] grid) {
        Deque<int[]> dq = new ArrayDeque<>();
        dq.add(new int[]{x, y, 0});

        while (!dq.isEmpty()) {
            int[] curr = dq.poll();

            if (curr[2] == 2) {
                if (grid[curr[0]][curr[1]] == 'P') return false;
            } else {
                for (int[] d : dir) {
                    int nextX = curr[0] + d[0];
                    int nextY = curr[1] + d[1];

                    if (0 <= nextX && nextX < 5 && 0 <= nextY && nextY < 5) {
                        if (grid[nextX][nextY] == 'P') return false;
                        else if (grid[nextX][nextY] == 'O') {
                            dq.add(new int[]{nextX, nextY, curr[2] + 1});
                        }
                    }
                }
            }
        }

        if (x > 0 && y < 4
                && (grid[x - 1][y] != 'X' || grid[x][y + 1] != 'X')
                && grid[x - 1][y + 1] == 'P'
        ) return false;
        return true;
    }

    public int isValid(String[] place) {
        char[][] grid = new char[5][5];

        for (int i = 0; i < 5; i++) {
            grid[i] = place[i].toCharArray();
        }

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (grid[i][j] == 'P' && !search(i, j, grid)) return 0;
            }
        }
        return 1;
    }

    public int[] solution(String[][] places) {
        int[] answer = new int[5];

        for (int i = 0; i < 5; i++) {
            answer[i] = isValid(places[i]);
        }
        return answer;
    }
}