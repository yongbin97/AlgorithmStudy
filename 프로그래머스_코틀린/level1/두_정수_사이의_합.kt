package 프로그래머스_코틀린.level1

class Solution11 {
    fun solution(a: Int, b: Int): Long {
        var answer: Long = 0

        var range = if (a >= b) b..a else a..b

        for (i in range){
            answer += i
        }
        return answer
    }
}