import java.util.*;

class Solution {
    int N;
    int max = Integer.MIN_VALUE;
    int[] answer;
    int[][] dices;
    List<Integer> group = new ArrayList<>();
    List<Integer> sum1;
    List<Integer> sum2;
    
    public void makeSumList(int depth, int[][] dices, int sum, List<Integer> arr) {
        if (depth == N / 2) {
            arr.add(sum);
            return;
        }
        
        for (int i = 0; i < 6; i++) {
            makeSumList(depth + 1, dices, sum + dices[depth][i], arr);
        }
    }
    
    public void setArr() {
        int[][] group1dices = new int[N / 2][6];
        int[][] group2dices = new int[N / 2][6];
        
        int a = 0, b = 0;
        for (int i = 1; i < N + 1; i++) {
            if (group.contains(i)){
                group1dices[a] = dices[i - 1];
                a++;
            } else {
                group2dices[b] = dices[i - 1];
                b++;
            }
        }
        
        sum1 = new ArrayList<>();
        sum2 = new ArrayList<>();
        makeSumList(0, group1dices, 0, sum1);
        makeSumList(0, group2dices, 0, sum2);
    }
    
    public int calculateWinningRate() {
        int count = 0;
        setArr();
        sum2.sort(Comparator.naturalOrder());
        
        for (int num: sum1) {
            int left = 0, right = sum2.size() - 1;
            
            int idx = Integer.MIN_VALUE;
            while (left <= right) {
                int mid = (left + right) / 2;
                
                if (sum2.get(mid) < num) {
                    left = mid + 1;
                    idx = Math.max(idx, mid);
                } else {
                    right = mid - 1;
                }
            }
            if (idx != Integer.MIN_VALUE) {
                count += idx + 1;
            }
        }
        return count;
    }
    
    public void getGroup(int depth, int s) {
        if (depth == N / 2) {
            int winning = calculateWinningRate();
            
            if(winning > max) {
                max = winning;
                answer = group.stream().mapToInt(Integer::intValue).toArray();
            }
            return;
        }
        
        for (int i = s; i < N + 1; i++) {
            group.add(i);
            getGroup(depth + 1, i + 1);
            group.remove(group.size() - 1);
        }
    }
    
    public int[] solution(int[][] dice) {
        N = dice.length;
        dices = dice;
        answer = new int[dice.length / 2];
        
        getGroup(0, 1);
        return answer;
    }
}