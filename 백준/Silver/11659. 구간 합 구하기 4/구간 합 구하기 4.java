import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();

    String[] row = br.readLine().split(" ");
    int N = Integer.parseInt(row[0]);
    int M = Integer.parseInt(row[1]);

    row = br.readLine().split(" ");
    int[] nums = new int[N];

    for (int i = 0; i < N; i++) {
      if (i == 0){
        nums[i] = Integer.parseInt(row[i]);
      } else {
        nums[i] = nums[i - 1] + Integer.parseInt(row[i]);
      }
    }

    for (int i = 0; i < M; i++) {
      row = br.readLine().split(" ");
      int left = Integer.parseInt(row[0]) - 1;
      int right = Integer.parseInt(row[1]) - 1;

      int sum = nums[right];
      if (left > 0) sum -= nums[left - 1];
      sb.append(sum).append("\n");
    }

    System.out.println(sb.toString().strip());
  }
}