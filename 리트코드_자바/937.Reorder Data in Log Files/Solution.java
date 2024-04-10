import java.util.ArrayList;
import java.util.List;

class Solution {
    public String[] reorderLogFiles(String[] logs) {
        List<String> letterList = new ArrayList<>();
        List<String> digitList = new ArrayList<>();

        // log 분류하기
        for (String log: logs){
            if (Character.isDigit(log.split(" ", 2)[1].charAt(0))){
                digitList.add(log);
            } else {
                letterList.add(log);
            }
        }

        // 문자 로그 정렬하기
        letterList.sort((s1, s2) -> {
            // 식별자, 식별자 제외 부분으로 나누기
            String[] s1x = s1.split(" ", 2);
            String[] s2x = s2.split(" ", 2);

            int compared = s1x[1].compareTo(s2x[1]);

            if (compared == 0){
                return s1x[0].compareTo(s2x[0]);
            } else {
                return compared;
            }
        });

        // 문자 로그 + 숫자 로그
        letterList.addAll(digitList);
        return letterList.toArray(new String[0]);
    }
}