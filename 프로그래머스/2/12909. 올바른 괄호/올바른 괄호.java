import java.util.*;


class Solution {
    boolean solution(String s) {
        int stackCount = 0;
        
        for (char c: s.toCharArray()){
            if (c == '('){
                stackCount += 1;
            } else {
                if (stackCount <= 0){
                    return false;
                }
                stackCount -= 1;
            }
        }
        return stackCount == 0;
    }
}