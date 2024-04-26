import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        // target이 words에 없으면 0을 리턴
        if (!Arrays.asList(words).contains(target)) {
            return 0;
        }

        // dfs로 탐색
        List<String> wordList = new ArrayList<>(Arrays.asList(words));
        wordList.remove(begin);
        int result = search(begin, target, wordList, 0);
        if (result > 50) return 0;
        else return result;
    }

    public int search(String curr, String target, List<String> words, int count) {
        if (words.size() == 0) {
            return 100;
        }

        if (curr.equals(target)) {
            return count;
        }

        int result = 100;
        for (String word : words) {
            if (getCountOfDiffChars(curr, word) == 1) {
                List<String> newWords = new ArrayList<>(words);
                newWords.remove(word);
                result = Math.min(result, search(word, target, newWords, count + 1));
            }
        }
        return result;
    }

    public int getCountOfDiffChars(String a, String b) {
        int count = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                count++;
            }
        }
        return count;
    }
}