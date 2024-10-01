import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine().strip());
    System.out.println(solution(N));

    br.close();
  }

  private static int solution(int n) {
    /*
     * f(n) = f(n - 1) + f(n - 2)
     * f(1) = 1
     * f(2) = 2
     */
    int[] dp = new int[1001];
    dp[1] = 1;
    dp[2] = 2;

    if (n < 3) {
      return dp[n];
    }

    for (int i = 3; i <= n; i++) {
      dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
    }

    return dp[n];
  }
}