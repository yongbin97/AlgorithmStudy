import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        Map<Integer, String> carTimeMap = new HashMap<>();
        Map<Integer, Integer> carTimeSumMap = new HashMap<>();
        Map<Integer, Integer> carFeeMap = new HashMap<>();
        
        for (String record: records) {
            String[] arr = record.split(" ");
            int carNum = Integer.parseInt(arr[1]);
            
            if (arr[2].equals("IN")) {
                carTimeMap.put(carNum, arr[0]);
            } else {
                carTimeSumMap.putIfAbsent(carNum, 0);
                carTimeSumMap.put(carNum, carTimeSumMap.get(carNum) + getTime(carTimeMap.get(carNum), arr[0]));
                carTimeMap.remove(carNum);
            }
        }
        for (int carNum: carTimeMap.keySet()) {
            carTimeSumMap.putIfAbsent(carNum, 0);
            carTimeSumMap.put(carNum, carTimeSumMap.get(carNum) + getTime(carTimeMap.get(carNum), "23:59"));
        }
        
        for (int carNum: carTimeSumMap.keySet()) {
            carFeeMap.put(carNum, getFee(fees, carTimeSumMap.get(carNum)));
        }
        
        List<Integer> keyset = new ArrayList<>(carFeeMap.keySet());
        Collections.sort(keyset);
        
        int[] answer = new int[keyset.size()];
        for (int i = 0; i < keyset.size(); i ++) {
            answer[i] = carFeeMap.get(keyset.get(i));
        }
        
        return answer;
    }
    
    public int getFee(int[] fees, int time) {
        int tmp = Math.max(0, time - fees[0]);
        
        int extraTime = tmp / fees[2];
        if (tmp % fees[2] != 0) {
            extraTime += 1;
        }        
        return fees[1] + extraTime * fees[3];
    }
    
    public int getTime(String inTime, String outTime) {
        return convert(outTime) - convert(inTime);
    }
    
    public int convert(String time) {
        int hour = Integer.parseInt(time.split("\\:")[0]);
        int min = Integer.parseInt(time.split("\\:")[1]);
        
        return hour * 60 + min;
    }
}