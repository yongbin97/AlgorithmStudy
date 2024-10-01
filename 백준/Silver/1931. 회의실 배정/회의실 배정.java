import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine().strip());
    int[][] timeArr = new int[N][2];

    for (int i = 0; i < N; i++) {
      String[] row = br.readLine().split(" ");
      int start = Integer.parseInt(row[0]);
      int end = Integer.parseInt(row[1]);
      timeArr[i] = new int[]{start, end};
    }

    Arrays.sort(timeArr, (o1, o2) -> {
      if (o1[1] == o2[1]) {
        return o1[0] - o2[0];
      } return o1[1] - o2[1];
    });

    int end = 0;
    int cnt = 0;
    for (int[] time : timeArr) {
      if (time[0] >= end) {
        end = time[1];
        cnt ++;
      }
    }
    System.out.println(cnt);
  }

}