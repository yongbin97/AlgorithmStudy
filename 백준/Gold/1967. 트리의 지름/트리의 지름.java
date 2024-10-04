import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  static class Node {
    int idx;
    int weight;
    List<Node> children;

    public Node(int idx, int weight) {
      this.idx = idx;
      this.weight = weight;
      this.children = new ArrayList<>();
    }

    public String toString() {
      return "Node" + this.idx;
    }
  }

  private static int answer = 0;
  private static Map<Integer, Node> nodeMap = new HashMap<>();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(br.readLine().strip());

    for (int i = 1; i <= n; i++) {
      nodeMap.put(i, new Node(i, 0));
    }

    Node root = nodeMap.get(1);

    for (int i = 0; i < n - 1; i++) {
      String[] input = br.readLine().split(" ");
      int parent = Integer.parseInt(input[0]);
      int child = Integer.parseInt(input[1]);
      int weight = Integer.parseInt(input[2]);

      Node parentNode = nodeMap.get(parent);
      Node childNode = nodeMap.get(child);
      childNode.weight = weight;
      parentNode.children.add(childNode);
    }
    dfs(root);
    System.out.println(answer);
  }

  private static int dfs(Node node) {
    if (node.children.isEmpty()) {
      return node.weight;
    }

    int top1 = 0;
    int top2 = 0;
    for (Node child: node.children) {
      int childPathWeight = dfs(child);
      if (childPathWeight > top1) {
        top2 = top1;
        top1 = childPathWeight;
      } else if (childPathWeight > top2) {
        top2 = childPathWeight;
      }
    }

    answer = Math.max(answer, top1 + top2);

    return top1 + node.weight;
  }
}
