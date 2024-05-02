import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    Map<Character, List<Character>> letterMap = new HashMap<>(){{
        put('2', List.of('a', 'b', 'c'));
        put('3', List.of('d', 'e', 'f'));
        put('4', List.of('g', 'h', 'i'));
        put('5', List.of('j', 'k', 'l'));
        put('6', List.of('m', 'n', 'o'));
        put('7', List.of('p', 'q', 'r', 's'));
        put('8', List.of('t', 'u', 'v'));
        put('9', List.of('w', 'x', 'y', 'z'));
    }};


    public List<String> letterCombinations(String digits) {
        List<String> answer = new ArrayList<>();
        if (digits.length() == 0) return answer;

        searchDFS(digits, 0, new StringBuilder(), answer);
        return answer;
    }

    public void searchDFS(String digits, int idx, StringBuilder path, List<String> answer){
        if (digits.length() == idx){
            answer.add(String.valueOf(path));
            return;
        }

        for (char c: letterMap.get(digits.charAt(idx))){
            searchDFS(digits, idx + 1, new StringBuilder(path).append(c), answer);
        }
    }
}