import java.util.*;

class Solution {
    public double[] solution(int k, int[][] ranges) {
        double[] answer = new double[ranges.length];        
        Map<Integer, Double> resultMap = new HashMap<>();
    
        int idx = 0;
        double dk = (double) k;
        double lastDk;
        
        while (dk != 1){
            lastDk = dk;
            if (dk % 2 == 1) dk = 3 * dk + 1;
            else dk = dk / 2;
            resultMap.put(idx, (dk + lastDk) / 2);
            idx ++;
        }

        for (int i = 0; i < ranges.length; i++){
            int[] range = ranges[i];
            int start = ranges[i][0];
            int end = idx + ranges[i][1];
            
            if (start > end) answer[i] = -1;
            else {
                double result = 0;
                for (int j = start; j < end; j++){
                    result += resultMap.get(j);
                }
                answer[i] = result;
            }
        }
        
        return answer;
    }
}