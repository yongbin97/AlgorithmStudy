import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine().strip());
        List<List<Integer>> edges = new ArrayList<>();

        for (int i = 0; i <= N; i++) {
            edges.add(new ArrayList<>());
        }

        for (int i = 0; i < N - 1; i++) {
            String[] row = br.readLine().split(" ");
            int u = Integer.parseInt(row[0]);
            int v = Integer.parseInt(row[1]);

            edges.get(u).add(v);
            edges.get(v).add(u);
        }

        int[] parent = new int[N + 1];

        // curr
        boolean[] visited = new boolean[N + 1];
        Deque<Integer> dq = new ArrayDeque<>();
        dq.add(1);
        visited[1] = true;

        while (!dq.isEmpty()) {
            int curr = dq.pollFirst();

            for (int next: edges.get(curr)) {
                if (!visited[next]) {
                    dq.add(next);
                    parent[next] = curr;
                    visited[next] = true;
                }
            }

        }

        for (int i = 2; i < N + 1; i++) {
            sb.append(parent[i]).append("\n");
        }
        System.out.println(sb.toString().strip());
    }
}