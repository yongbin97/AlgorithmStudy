import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        Map<String, Integer> map = new HashMap<>();
        map.put("code", 0);
        map.put("date", 1);
        map.put("maximum", 2);
        map.put("remain", 3);
        
        int extIdx = map.get(ext);
        int sortIdx = map.get(sort_by);
        
        int[][] filteredData = Arrays.stream(data)
            .filter(d -> d[extIdx] < val_ext)
            .sorted((o1, o2) -> o1[sortIdx] - o2[sortIdx])
            .toArray(int[][]::new);
        
        return filteredData;
    }
}