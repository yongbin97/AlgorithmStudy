import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine().strip());

        PriorityQueue<Integer> maxPQ = new PriorityQueue<>(Comparator.reverseOrder());
        PriorityQueue<Integer> minPQ = new PriorityQueue<>();

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine().strip());
            if (i % 2 == 0) {
                maxPQ.add(num);
            } else {
                minPQ.add(num);
            }

            if (!maxPQ.isEmpty() && !minPQ.isEmpty() && maxPQ.peek() > minPQ.peek()) {
                int big = maxPQ.poll();
                int small = minPQ.poll();

                maxPQ.add(small);
                minPQ.add(big);
            }
            System.out.println(maxPQ.peek());
        }

    }

}
