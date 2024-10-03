import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  public static long C;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String[] row = br.readLine().split(" ");

    long A = Long.parseLong(row[0]);
    long B = Long.parseLong(row[1]);
    C = Long.parseLong(row[2]);

    System.out.println(calc(A, B));
  }

  public static long calc(long A, long num) {
    if (num == 1) {
      return A % C;
    }

    long tmp = calc(A, num / 2) % C;

    if (num % 2 == 0) {
      return tmp * tmp % C;
    } else {
      return (tmp * A % C) * tmp % C;
    }
  }
}
