import java.util.ArrayList;
import java.util.List;

class Solution {

    public String[] solution(String[][] tickets) {
        return searchPath("ICN", List.of(tickets)).toArray(new String[0]);
    }

    public List<String> searchPath(String currentCity, List<String[]> tickets){
        if (tickets.size() == 0){
            List<String> path = new ArrayList<>();
            path.add(currentCity);
            return path;
        }

        List<String[]> nextTickets = getNextTickets(currentCity, tickets);
        List<List<String>> pathList = new ArrayList<>();

        for (String[] ticket: nextTickets){
            List<String[]> remainTickets = new ArrayList<>(tickets);
            remainTickets.remove(ticket);

            List<String> path = searchPath(ticket[1], remainTickets);
            if (path != null){
                path.add(0, currentCity);
                pathList.add(path);
            }
        }

        //pathList 알파벳 순으로 정렬
        pathList.sort((o1, o2) -> {
            for (int i = 0; i < o1.size(); i++){
                if (o1.get(i).compareTo(o2.get(i)) != 0){
                    return o1.get(i).compareTo(o2.get(i));
                }
            }
            return 0;
        });
        if (pathList.size() > 0){
            return pathList.get(0);
        } else {
            return null;
        }
    }

    public List<String[]> getNextTickets(String currentCity, List<String[]> remainTickets){
        List<String[]> nextTickets = new ArrayList<>();

        for(String[] ticket : remainTickets){
            if(ticket[0].equals(currentCity)){
                nextTickets.add(ticket);
            }
        }

        return nextTickets;
    }
}