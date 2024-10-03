import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

  public static int N;
  public static int M;
  public static int[] nums;
  public static boolean[] visited;
  public static Set<String> resultSet = new LinkedHashSet<>();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();

    String[] row = br.readLine().split(" ");
    N = Integer.parseInt(row[0]);
    M = Integer.parseInt(row[1]);

    nums = new int[N];
    visited = new boolean[N];

    row = br.readLine().split(" ");
    for (int i = 0; i < N; i++) {
      nums[i] = Integer.parseInt(row[i]);
    }
    Arrays.sort(nums);

    permutation(M, new ArrayList<>());

    for (String str: resultSet) {
      sb.append(str).append("\n");
    }
    System.out.println(sb.toString().strip());
  }

  public static void permutation(int depth, List<Integer> selected) {
    if (depth == 0) {
      resultSet.add(selected.stream().map(String::valueOf).collect(Collectors.joining(" ")));
      return;
    }

    for (int i = 0; i < N; i++) {
      if (visited[i]) {
        continue;
      }

      selected.add(nums[i]);
      visited[i] = true;

      permutation(depth - 1, selected);

      selected.remove(selected.size() - 1);
      visited[i] = false;
    }
  }

}
