package 프로그래머스_코틀린.level2

class Solution1 {
    fun solution(citations: IntArray): Int {
        var max = 0

        for (idx in citations.indices){
            val numOfPaper = citations.count{it >= idx + 1}
            if (numOfPaper >= idx + 1 && idx + 1 >= max){
                max = idx + 1
            }
        }
        return max
    }
}