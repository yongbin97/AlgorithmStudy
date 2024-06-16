class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Map<String, Integer> wordCountMap = new HashMap<>();

        for (String word : paragraph.toLowerCase().replaceAll("[^a-zA-Z]+", " ").split(" ")) {
            if (!Arrays.asList(banned).contains(word)) {
                int count = wordCountMap.getOrDefault(word, 0);
                wordCountMap.put(word.toLowerCase(), count + 1);
            }
        }

        return Collections.max(wordCountMap.entrySet(), Map.Entry.comparingByValue()).getKey();
    }
}