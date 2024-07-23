import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int convert(String date) {
        int year = Integer.parseInt(date.split("\\.")[0]);
        int month = Integer.parseInt(date.split("\\.")[1]);
        int day = Integer.parseInt(date.split("\\.")[2]);
        
        return year * 12 * 28 + month * 28 + day;
    }
    
    public boolean isExpired(String today, String date, int month) {
        int todayInt = convert(today);
        int dateInt = convert(date) + month * 28 - 1;
        
        return todayInt > dateInt;
    }

    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> answ = new ArrayList<>();
        
        Map<String, Integer> termMap = new HashMap<>();
        for (String term: terms) {
            String[] arr = term.split(" ");
            termMap.put(arr[0], Integer.parseInt(arr[1]));
        }
        
        for (int i = 1; i < privacies.length + 1; i++) {
            String[] priv = privacies[i - 1].split(" ");
            if (isExpired(today, priv[0], termMap.get(priv[1]))){
                answ.add(i);
            }
            
        }
        return answ.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}