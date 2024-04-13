import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> group = new HashMap<>();

        for (String str: strs){
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String key = String.valueOf(chars);

            List<String> anagramList = group.getOrDefault(key, new ArrayList<>());
            anagramList.add(str);
            group.put(key, anagramList);
        }
        return new ArrayList<>(group.values());
    }
}