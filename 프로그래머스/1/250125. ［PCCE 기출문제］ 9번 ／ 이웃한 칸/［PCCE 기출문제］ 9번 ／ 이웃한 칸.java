class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        
        int[][] dirs = new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        
        int nextH, nextW;
        for (int[] dir: dirs){
            nextH = h + dir[0];
            nextW = w + dir[1];
            
            if (nextH >= 0 && nextH < board.length && nextW >= 0 && nextW < board.length) {
                if (board[h][w].equals(board[nextH][nextW])) answer ++;
            }
        }
        
        return answer;
    }
}