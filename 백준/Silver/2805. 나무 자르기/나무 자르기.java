import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

  private static int M;
  private static int N;
  private static int[] trees;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String[] row = br.readLine().split(" ");
    N = Integer.parseInt(row[0]);

    M = Integer.parseInt(row[1]);
    trees = new int[N];

    row = br.readLine().split(" ");
    for (int i = 0; i < N; i++) {
      trees[i] = Integer.parseInt(row[i]);
    }
    Arrays.sort(trees);

    System.out.println(solution());
  }

  private static int solution() {
    int left = 0;
    int right = trees[N - 1];
    int answer = 0;

    while (left <= right) {
      int mid = (left + right) / 2;

      if (cut(mid) >= M) {
        answer = Math.max(answer, mid);

        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    return answer;
  }

  private static long cut(int h) {
    long sum = 0;

    for (int i = N - 1; i >= 0; i--) {
      if (trees[i] > h) {
        sum += trees[i] - h;
      }
    }

    return sum;
  }
}