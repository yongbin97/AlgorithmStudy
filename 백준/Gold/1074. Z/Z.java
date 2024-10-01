import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] row = br.readLine().split(" ");
    int N = Integer.parseInt(row[0]);
    int r = Integer.parseInt(row[1]);
    int c = Integer.parseInt(row[2]);

    int len = (int) Math.pow(2, N);
    int[] point = new int[]{0, 0};
    int value = 0;

    while (len > 2) {
      int x = point[0], y = point[1];
      int pointValue = value;

      int add = (int) Math.pow((double) len / 2, 2);

      for (int i = x; i < x + len; i += len / 2) {
        for (int j = y; j < y + len; j += len / 2) {
          if (r >= i && c >= j) {
            point[0] = i;
            point[1] = j;
            value = pointValue;
          }
          pointValue += add;
        }
      }
      len /= 2;
    }

    int answer = 0;
    for (int i = 0; i <= 1; i++) {
      for (int j = 0; j <= 1; j++) {
        if (point[0] + i == r && point[1] + j == c) {
          answer = value;
        }
        value ++;
      }
    }

    System.out.println(answer);
  }
}
