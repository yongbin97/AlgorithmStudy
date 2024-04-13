import java.util.*;
import java.util.stream.Stream;


class Solution2 {
    public String expand(int left, int right, String s){
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){
            left--;
            right++;
        }

        return s.substring(left + 1, right);
    }

    public String longestPalindrome(String s) {
        if (s.length() < 2){
            return s;
        }

        String result = "";
        for (int i=0; i < s.length(); i++){
            result = Stream.of(expand(i, i, s), expand(i, i+1, s), result)
                    .max(Comparator.comparingInt(String::length))
                    .orElse("");
        }

        return result;
    }
}