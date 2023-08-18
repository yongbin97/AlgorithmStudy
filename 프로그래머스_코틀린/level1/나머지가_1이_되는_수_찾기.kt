package 프로그래머스_코틀린.level1

class Solution5 {
    fun solution(n: Int): Int {
        for (it in 1..n){
            if (n % it == 1){
                return it
            }
        }
        return n
    }
}