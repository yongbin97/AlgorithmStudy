import java.util.*;

class Solution {
    public int[] solution(String[] park, String[] routes) {
        int currX = 0;
        int currY = 0;
        
        for (int i=0; i < park.length; i ++){
            if (park[i].indexOf('S') != -1){
                currX = i;
                currY = park[i].indexOf('S');
                break;
            }
        }
        
        Map<String, int[]> directionMap = new HashMap<>();
        directionMap.put("N", new int[]{-1, 0});
        directionMap.put("S", new int[]{1, 0});
        directionMap.put("W", new int[]{0, -1});
        directionMap.put("E", new int[]{0, 1});
        
        
        // 명령 수행
        for (String route: routes){
            String[] command = route.split(" ");
            String dir = command[0];
            int dist = Integer.valueOf(command[1]);
            int[] direction = directionMap.get(dir);
            
            if (canMove(currX, currY, direction, dist, park)){
                currX += direction[0] * dist;
                currY += direction[1] * dist;
            }
        }
        return new int[]{currX, currY};
    }
    
    public boolean canMove(int x, int y, int[] direction, int dist, String[] park){
        int tempX = x;
        int tempY = y;
        
        for (int i=0; i < dist; i ++){
            tempX += direction[0];
            tempY += direction[1];
            
            if (
                0 <= tempX
                && tempX < park.length 
                && 0 <= tempY
                && tempY < park[0].length()
            ){
                if (park[tempX].charAt(tempY) == 'X'){
                    return false;
                }
            }
            else {
                return false;
            }
        }
        return true;
    }
}