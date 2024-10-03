import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine().strip());

    int[][] price = new int[N][3];

    for (int i = 0; i < N; i++) {
      String[] row = br.readLine().split(" ");
      price[i][0] = Integer.parseInt(row[0]);
      price[i][1] = Integer.parseInt(row[1]);
      price[i][2] = Integer.parseInt(row[2]);
    }

    int[][] dp = new int[N][3];
    dp[0][0] = price[0][0];
    dp[0][1] = price[0][1];
    dp[0][2] = price[0][2];

    for (int i = 1; i < N; i++) {
      for (int j = 0; j < 3; j++) {
        dp[i][j] = Math.min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + price[i][j];
      }
    }

    int answer = Integer.MAX_VALUE;
    for (int i = 0; i < 3; i++) {
      answer = Math.min(answer, dp[N - 1][i]);
    }

    System.out.println(answer);
  }

}
