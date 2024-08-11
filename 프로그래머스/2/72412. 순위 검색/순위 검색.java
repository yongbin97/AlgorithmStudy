import java.util.*;

class Solution {
    Map<String, List<Integer>> infoMap = new HashMap<>();
    
    public void dfs(int depth, String query, String[] info) {
        if (depth == 4) {
            if (!infoMap.containsKey(query)) {
                List<Integer> scores = new ArrayList<>();
                scores.add(Integer.parseInt(info[4]));
                infoMap.put(query, scores);
            } else {
                infoMap.get(query).add(Integer.parseInt(info[4]));
            }
            return;
        }
        
        dfs(depth + 1, query + "-", info);
        dfs(depth + 1, query + info[depth], info);
    }
    
    public int[] solution(String[] info, String[] query) {
        int[] answer = new int[query.length];
        
        for (String data: info){
            dfs(0, "", data.split(" "));
        }
        
        for (List<Integer> values : infoMap.values()) {
            Collections.sort(values);
        }
        
        for (int i = 0; i < query.length; i++) {
            String[] qArr = query[i].split(" ");
            
            String req = qArr[0] + qArr[2] + qArr[4] + qArr[6];
            int target = Integer.parseInt(qArr[7]);
            
            if (infoMap.containsKey(req)) {
                List<Integer> score = infoMap.get(req);
                int left = 0, right = score.size() - 1;
                
                while (left <= right) {
                    int mid = (left + right) / 2;
                    
                    if (score.get(mid) < target) left = mid + 1;
                    else right = mid - 1;
                }              
                
                answer[i] = score.size() - left;
            }
        }
        
        
        return answer;
    }
    

}