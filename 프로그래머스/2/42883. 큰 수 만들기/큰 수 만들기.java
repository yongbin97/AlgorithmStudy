import java.util.Deque;
import java.util.LinkedList;
import java.util.stream.Collectors;

class Solution {
    public String solution(String number, int k) {
        Deque<Character> stack = new LinkedList<>();

        for (char num: number.toCharArray()) {
            while (!stack.isEmpty() && k > 0 && stack.peekLast() - '0' < num - '0') {
                stack.pollLast();
                k--;
            }
            stack.add(num);
        }

        while (k > 0) {
            stack.pollLast();
            k--;
        }

        return stack.stream()
                .map(Object::toString)
                .collect(Collectors.joining());
    }
}