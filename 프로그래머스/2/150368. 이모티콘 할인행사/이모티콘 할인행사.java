import java.util.*;

class Solution {
    int ePlus = 0;
    int total = 0;
    
    public int[] solution(int[][] users, int[] emoticons) {
        int[] answer = new int[2];
        getPrice(0, new int[emoticons.length], emoticons, users);
        answer[0] = ePlus;
        answer[1] = total;
        return answer;
    }
    
    public void getPrice(int idx, int[] rate, int[] emoticons, int[][] users) {
        if (idx == emoticons.length) { 
            update(rate, emoticons, users);
            return;
        }
        
        for (int i = 1; i < 5; i++) {
            rate[idx] = i * 10;
            getPrice(idx + 1, rate, emoticons, users);
        }
    }
    
    public void update(int[] rate, int[] emoticons, int[][] users) {
        int currPlus = 0;
        int currTotal = 0;
        
        for (int[] user: users) {
            int sale = 0;
            for (int i = 0; i < emoticons.length; i++) {
                if (rate[i] >= user[0]) {
                    sale += emoticons[i] * (100 - rate[i]) / 100;
                } 
                if (sale >= user[1]) {
                    currPlus += 1;
                    sale = 0;
                    break;
                }
            }
            currTotal += sale;
        }
        
        if (currPlus > ePlus) {
            ePlus = currPlus;
            total = currTotal;
        } else if (currPlus == ePlus) {
            total = Math.max(total, currTotal);
        }
    }
}