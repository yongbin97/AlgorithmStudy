package 프로그래머스_코틀린.level1

class Solution21 {
    fun solution(a: IntArray, b: IntArray): Int {
        var answer: Int = 0
        for ((idx, value) in a.withIndex()){
            answer += value * b[idx]
        }
        return answer
    }
}