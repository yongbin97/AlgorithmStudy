import java.util.*;

class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        
        String convertN = convert(n, k);
        String[] arr = convertN.split("0");
        
        for (String s: arr) {
            if (s.equals("")) continue;
            if (isPrime(Long.parseLong(s))) answer ++;
        }
        
        return answer;
    }
    
    public boolean isPrime(Long x) {
        if (x == 1) return false;
        for (long i = 2; i * i <= x; i++) {
            if (x % i == 0) return false;
        }
        return true;
    }
    
    public String convert(int n, int k) {
        StringBuilder sb = new StringBuilder();
        
        while (n > 0) {
            sb.append(Integer.toString(n % k));
            n = n / k;
        }
        
        return sb.reverse().toString();
    }
}