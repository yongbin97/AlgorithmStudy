import java.util.*;


class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> {
            if (getDistance(o1) > getDistance(o2)) return 1;
            else if (getDistance(o1) == getDistance(o2)) return 0;
            else return -1;
        });

        for (int[] point : points) {
            pq.add(point);
        }

        int[][] result = new int[k][2];
        for (int i = 0; i < k; i++) {
            result[i] = pq.poll();
        }
        return result;
    }

    public int getDistance(int[] point) {
        return point[0] * point[0] + point[1] * point[1];
    }
}