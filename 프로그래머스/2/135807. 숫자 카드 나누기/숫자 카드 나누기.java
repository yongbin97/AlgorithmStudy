import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        List<Integer> commonDivisorA = getCommonDivisor(arrayA);
        List<Integer> commonDivisorB = getCommonDivisor(arrayB);

        return Math.max(getMaximum(commonDivisorA, arrayB), getMaximum(commonDivisorB, arrayA));
    }

    // arr안의 숫자들을 모두 나눌 수 없는 가장 큰 숫자 찾기
    public int getMaximum(List<Integer> commonDivisor, int[] arr) {
        for (int divisor : commonDivisor) {
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] % divisor == 0) {
                    break;
                }
                if (i == arr.length - 1) {
                    return divisor;
                }
            }
        }
        return 0;
    }

    // arr안에 있는 숫자들의 공약수 구하기
    public List<Integer> getCommonDivisor(int[] arr) {
        Arrays.sort(arr);

        List<Integer> divisors = new ArrayList<>();

        for (int i = 2; i <= arr[0]; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (arr[j] % i != 0) {
                    break;
                }
                if (j == arr.length - 1) {
                    divisors.add(i);
                }
            }
        }
        divisors.sort(Comparator.comparing(Integer::intValue).reversed());
        return divisors;
    }
}