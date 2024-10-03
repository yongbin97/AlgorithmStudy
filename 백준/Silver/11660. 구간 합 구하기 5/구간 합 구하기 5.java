import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  private static int[][] graph;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();

    String[] row = br.readLine().split(" ");
    int N = Integer.parseInt(row[0]);
    int M = Integer.parseInt(row[1]);

    graph = new int[N][N];
    for (int i = 0; i < N; i++) {
      row = br.readLine().split(" ");

      for (int j = 0; j < N; j++) {
        graph[i][j] = Integer.parseInt(row[j]);

        if (i > 0) {
          graph[i][j] += graph[i - 1][j];
        }
        if (j > 0) {
          graph[i][j] += graph[i][j - 1];
        }
        if (i > 0 && j > 0) {
          graph[i][j] -= graph[i - 1][j - 1];
        }
      }
    }

    int[][] operation = new int[M][4];
    for (int i = 0; i < M; i++) {
      row = br.readLine().split(" ");

      for (int j = 0; j < 4; j++) {
        operation[i][j] = Integer.parseInt(row[j]) - 1;
      }
    }

    for (int[] op : operation) {
      sb.append(getSum(op)).append("\n");
    }

    System.out.println(sb.toString().strip());

  }

  private static int getSum(int[] op) {
    int x1 = op[0];
    int y1 = op[1];
    int x2 = op[2];
    int y2 = op[3];

    int sum = graph[x2][y2];

    if (x1 > 0) {
      sum -= graph[x1 - 1][y2];
    }
    if (y1 > 0) {
      sum -= graph[x2][y1 - 1];
    }
    if (x1 > 0 && y1 > 0) {
      sum += graph[x1 - 1][y1 - 1];
    }
    return sum;
  }
}
