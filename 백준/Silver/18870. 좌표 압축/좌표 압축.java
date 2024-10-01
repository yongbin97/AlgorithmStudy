import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();

    int N = Integer.parseInt(br.readLine().strip());
    String[] row = br.readLine().split(" ");

    Set<Integer> nums = new HashSet<>();

    for (String ele: row) {
      nums.add(Integer.parseInt(ele));
    }

    List<Integer> list = new ArrayList<>(nums);
    list.sort(Comparator.naturalOrder());

    Map<Integer, Integer> rankMap = new HashMap<>();
    for (int i = 0; i < list.size(); i++) {
      rankMap.put(list.get(i), i);
    }

    for (String ele: row) {
      sb.append(rankMap.get(Integer.parseInt(ele))).append(" ");
    }

    System.out.println(sb.toString().strip());

  }

}