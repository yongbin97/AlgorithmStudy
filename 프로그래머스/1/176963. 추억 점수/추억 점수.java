import java.util.*;


class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int photoLength = photo.length;
        int[] answer = new int[photoLength];
        
        Map<String, Integer> yearningMap = new HashMap<>();
        
        for (int i=0; i < name.length; i++){
            yearningMap.put(name[i], yearning[i]);
        }
        
        for (int i=0; i < photo.length; i++){
            int sumOfYearning = 0;
            for (String person : photo[i]){
                sumOfYearning += yearningMap.getOrDefault(person, 0);
            }
            answer[i] = sumOfYearning;
        }
        
        return answer;
    }
}