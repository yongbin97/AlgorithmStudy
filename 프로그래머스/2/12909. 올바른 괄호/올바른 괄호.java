import java.util.*;

class Solution {
    boolean solution(String s) {
        Deque<Character> dq = new ArrayDeque<>();
        
        for (Character c: s.toCharArray()) {
            if (c == '(') {
                dq.push(c);
            } else {
                if (dq.poll() == null) {
                    return false;
                }
            }
        }
        if (dq.isEmpty()) {
            return true;
        } else {
            return false;
        }
    }
}