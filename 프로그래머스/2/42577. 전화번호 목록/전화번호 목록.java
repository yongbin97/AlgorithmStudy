import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        // Arrays.sort(phone_book, (o1, o2) -> {
        //     return o1.length() - o2.length();
        // });
        Arrays.sort(phone_book);
        
        System.out.println(Arrays.toString(phone_book));
        
        
        return answer;
    }
}