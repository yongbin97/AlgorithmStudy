import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int T = Integer.parseInt(br.readLine().strip());

    for (int i = 0; i < T; i++) {
      int n = Integer.parseInt(br.readLine().strip());
      int[][] scores = new int[2][n];

      for (int j = 0; j < 2; j++) {
        String[] row = br.readLine().split(" ");
        for (int l = 0; l < n; l++) {
          scores[j][l] = Integer.parseInt(row[l]);
        }
      }
      System.out.println(solution(n, scores));
    }
  }

  private static int solution(int n, int[][] scores) {
    int[][] dp = new int[2][n];

    for (int i = 0; i < n; i++) {
      if (i == 0) {
        dp[0][0] = scores[0][0];
        dp[1][0] = scores[1][0];
      } else if (i == 1) {
        dp[0][1] = dp[1][0] + scores[0][1];
        dp[1][1] = dp[0][0] + scores[1][1];
      } else {
        for (int j = 0; j < 2; j++) {
          dp[j][i] = Math.max(dp[1 - j][i - 1], dp[1 - j][i - 2]) + scores[j][i];
        }
      }
    }
    return Math.max(dp[0][n - 1], dp[1][n - 1]);
  }
}
