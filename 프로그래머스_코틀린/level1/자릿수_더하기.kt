package 프로그래머스_코틀린.level1

class Solution4 {
    fun solution(n: Int): Int {
        var answer = 0

        for (s in n.toString()){
            answer += s - '0'
        }

        return answer
    }
}