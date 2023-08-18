package 프로그래머스_코틀린.level1

class Solution1 {
    fun solution(n: Int): Int {
        var answer = 0

        for(it in 1..n){
            if(n%it == 0){
                answer += it
            }
        }
        return answer
    }
}