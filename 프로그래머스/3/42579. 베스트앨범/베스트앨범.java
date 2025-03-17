import java.util.*;

class Solution {
    
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answerList = new ArrayList<>();
        
        // id: play
        Map<Integer, Integer> musicMap = new HashMap<>();
        // genre: sum(play)
        Map<String, Integer> genreMap = new HashMap<>();
        // genre: [id]
        Map<String, List<Integer>> genreMusicMap = new HashMap<>();
        
        // set maps
        for (int i = 0; i < genres.length; i++) {
            String genre = genres[i];
            int play = plays[i];
            
            musicMap.put(i, play);
            genreMap.put(genre, genreMap.getOrDefault(genre, 0) + play);
            
            List<Integer> idList = genreMusicMap.getOrDefault(genre, new ArrayList<>());
            idList.add(i);
            genreMusicMap.put(genre, idList);
        }
        
        List<String> keySet = new ArrayList<>(genreMap.keySet());
        keySet.sort((o1, o2) -> genreMap.get(o2).compareTo(genreMap.get(o1)));
        
        for (String genre: keySet) {
            List<Integer> idList = genreMusicMap.get(genre);
            idList.sort((o1, o2) -> {
                if (musicMap.get(o1) == musicMap.get(o2)) {
                    return o2.compareTo(o1);
                } else {
                    return musicMap.get(o2).compareTo(musicMap.get(o1));
                }
            });
            
            answerList.add(idList.get(0));
            if (idList.size() > 1) {
                answerList.add(idList.get(1));    
            }
        }
        
        return answerList.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}