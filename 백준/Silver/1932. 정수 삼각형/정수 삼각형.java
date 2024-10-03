import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine().strip());
    int[][] maps = new int[N][N];

    for (int i = 0; i < N; i++) {
      String[] row = br.readLine().split(" ");
      for (int j = 0; j < row.length; j ++) {
        maps[i][j] = Integer.parseInt(row[j]);
      }
    }

    int[][] dp = new int[N][N];
    dp[0][0] = maps[0][0];

    for (int i = 1; i < N; i++) {
      for (int j = 0; j <= i; j++) {
        if (j > 0){
          dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i - 1][j]) + maps[i][j];
        } else {
          dp[i][j] = dp[i - 1][j] + maps[i][j];
        }
      }
    }
    int answer = 0;
    for (int i = 0; i < N; i++) {
      answer = Math.max(answer, dp[N - 1][i]);
    }
    System.out.println(answer);
  }
}
