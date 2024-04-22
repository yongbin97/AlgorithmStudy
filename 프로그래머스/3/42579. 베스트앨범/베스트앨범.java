import java.util.*;


class Solution {
    class Song {
        int idx;
        int play;
        
        public Song(int idx, int play){
            this.idx = idx;
            this.play = play;
        }
    }
    
    public int[] solution(String[] genres, int[] plays) {        
        Map<String, Integer> genrePlayMap = new HashMap<>();
        Map<String, PriorityQueue<Song>> genreSongMap = new HashMap<>();
        
        for (int i = 0; i < genres.length; i++){
            // 장르별 재생 수 기록하기
            genrePlayMap.put(genres[i], genrePlayMap.getOrDefault(genres[i], 0) + plays[i]);
            
            // 장르별 노래 PQ에 넣기
            Song newSong = new Song(i, plays[i]);
            PriorityQueue songList = genreSongMap.getOrDefault(genres[i], new PriorityQueue<Song>((s1, s2) -> {
                if (s1.play != s2.play) return s2.play - s1.play;
                else return s1.idx - s2.idx;
            }));
            songList.offer(newSong);
            genreSongMap.put(genres[i], songList);
        }
        
        List<Integer> answer = new ArrayList<>();
        
        List<Map.Entry<String, Integer>> entryList = new LinkedList<>(genrePlayMap.entrySet());
        entryList.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));
        
        for (Map.Entry<String, Integer> entry: entryList){
            String genre = entry.getKey();
            for (int i = 0; i < 2; i++){
                if (!genreSongMap.get(genre).isEmpty()){
                    answer.add(genreSongMap.get(genre).poll().idx);
                }
            }
        }
        
        return answer.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}