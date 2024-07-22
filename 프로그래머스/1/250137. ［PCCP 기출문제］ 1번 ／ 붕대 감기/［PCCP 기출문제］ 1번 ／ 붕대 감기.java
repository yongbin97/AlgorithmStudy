import java.util.*;

class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int time = 0;
        int curr = health;
        for (int[] attack: attacks) {
            curr += (attack[0] - time - 1) * bandage[1];
            if (attack[0] - time >= bandage[0]){
                curr += bandage[2] * ((attack[0] - time - 1) / bandage[0]);
            }
            if (curr >= health) curr = health;

            curr -= attack[1];
            time = attack[0];
            if (curr <= 0) return -1;
        }
        
        return curr;
    }
}