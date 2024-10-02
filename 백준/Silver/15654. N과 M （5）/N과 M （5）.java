import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


public class Main {
    public static int N;
    public static int M;
    public static int[] nums;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] row = br.readLine().split(" ");
        N = Integer.parseInt(row[0]);
        M = Integer.parseInt(row[1]);

        nums = new int[N];
        row = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(row[i]);
        }
        Arrays.sort(nums);

        comb(M, new ArrayList<>());
        System.out.println(sb.toString().strip());
    }

    public static void comb(int depth, List<Integer> list) {
        if (depth == 0) {
            String res = list.stream().map(String::valueOf).collect(Collectors.joining(" "));
            sb.append(res).append("\n");
            return;
        }

        for (int i = 0; i < N; i++) {
            if (!list.contains((Object) nums[i])) {
                list.add(nums[i]);
                comb(depth - 1, list);
                list.remove((Object) nums[i]);
            }
        }
    }

}