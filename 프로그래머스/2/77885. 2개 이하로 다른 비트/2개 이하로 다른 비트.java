class Solution {
    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];

        for (int i = 0; i < numbers.length; i++) {
            answer[i] = getNextNum(numbers[i]);
        }
        return answer;
    }

    public long getNextNum(long num) {
        if (num % 2 == 0) return num + 1;

        String bits = convert(num);
        for (int i = 0; i < bits.length();  i ++) {
            if (bits.charAt(bits.length() - i - 1) == '0') {
                return (long) (num + Math.pow(2, i) - Math.pow(2, i - 1));
            }
        }

        return -1;
    }

    public String convert(long number) {
        StringBuilder sb = new StringBuilder();
        while (number > 0) {
            sb.insert(0, number % 2);
            number = (number - number % 2) / 2;
        }
        sb.insert(0, 0);
        return sb.toString();
    }

}