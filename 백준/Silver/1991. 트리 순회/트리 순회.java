import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  public static Map<String, String[]> treeMap = new HashMap<>();
  public static StringBuilder sb = new StringBuilder();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine().strip());

    for (int i = 0; i < N; i++) {
      String[] row = br.readLine().split(" ");
      String node = row[0];
      String left = !Objects.equals(row[1], ".") ? row[1] : null;
      String right = !Objects.equals(row[2], ".") ? row[2] : null;
      treeMap.put(node, new String[]{left, right});
    }

    preorder("A");
    sb.append("\n");
    inorder("A");
    sb.append("\n");
    postorder("A");

    System.out.println(sb);

  }

  private static void preorder(String node) {
    if (node == null) return;

    String[] children = treeMap.get(node);

    sb.append(node);
    preorder(children[0]);
    preorder(children[1]);
  }

  private static void inorder(String node) {
    if (node == null) return;

    String[] children = treeMap.get(node);

    inorder(children[0]);
    sb.append(node);
    inorder(children[1]);
  }

  private static void postorder(String node) {
    if (node == null) return;

    String[] children = treeMap.get(node);

    postorder(children[0]);
    postorder(children[1]);
    sb.append(node);
  }
}
