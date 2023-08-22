package 프로그래머스_코틀린.level1

class Solution39 {
    fun solution(a: Int, b: Int, n: Int): Int {
        var answer: Int = 0
        var total: Int = n
        while (total >= a){
            answer += (total / a) * b
            total = (total / a) * b + (total % a)
        }
        return answer
    }
}