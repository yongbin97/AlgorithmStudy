import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


public class Main {
    public static int N;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] row = br.readLine().split(" ");
        N = Integer.parseInt(row[0]);
        int M = Integer.parseInt(row[1]);

        comb(1, M, new ArrayList<>());
        System.out.println(sb.toString().strip());
    }

    public static void comb(int num, int depth, List<Integer> list) {
        if (depth == 0) {
            String res = list.stream().map(String::valueOf).collect(Collectors.joining(" "));
            sb.append(res).append("\n");
            return;
        }

        for (int i = num; i <= N - depth + 1; i++) {
            list.add(i);
            comb(i + 1, depth - 1, list);
            list.remove(list.size() - 1);
        }
    }

}