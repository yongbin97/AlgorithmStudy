import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {

  private static PriorityQueue<Integer> heap = new PriorityQueue<>();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();

    int N = Integer.parseInt(br.readLine().strip());

    for (int i = 0; i < N; i++) {
      int op = Integer.parseInt(br.readLine().strip());
      if (op == 0) {
        if (heap.isEmpty()) {
          sb.append(0).append("\n");
        } else {
          sb.append(heap.poll()).append("\n");
        }
      } else {
        heap.add(op);
      }
    }

    System.out.println(sb.toString().strip());
  }
}