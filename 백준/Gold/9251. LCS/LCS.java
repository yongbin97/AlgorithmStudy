import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    char[] str1 = br.readLine().strip().toCharArray();
    char[] str2 = br.readLine().strip().toCharArray();

    int N = str1.length;
    int M = str2.length;

    int[][] LCS = new int[N + 1][M + 1];

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if (str1[i] == str2[j]) {
          LCS[i + 1][j + 1] = LCS[i][j] + 1;
        } else {
          LCS[i + 1][j + 1] = Math.max(LCS[i][j + 1], LCS[i + 1][j]);
        }
      }
    }
    System.out.println(LCS[N][M]);
  }
}
