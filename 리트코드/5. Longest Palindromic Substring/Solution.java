import java.util.*;


class Solution {
    public String expand(int left, int right, String s){
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){
            left--;
            right++;
        }

        return s.substring(left + 1, right);
    }

    public String longestString(String str1, String str2, String str3){
        List<String> stringList = new ArrayList<>();
        stringList.add(str1);
        stringList.add(str2);
        stringList.add(str3);

        stringList.sort(Comparator.comparing(String::length));
        return stringList.get(stringList.size() - 1);
    }

    public String longestPalindrome(String s) {
        if (s.length() < 2){
            return s;
        }

        String result = "";
        for (int i=0; i < s.length(); i++){
            result = longestString(expand(i, i, s), expand(i, i+1, s), result);
        }

        return result;
    }
}