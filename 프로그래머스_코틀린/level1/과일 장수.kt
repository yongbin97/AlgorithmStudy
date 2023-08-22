package 프로그래머스_코틀린.level1

class Solution43 {
    fun solution(k: Int, m: Int, score: IntArray): Int {
        var answer: Int = 0
        var sortedScoreList = score.toMutableList().sortedByDescending{it}
        var sumScore = 0
        for (i in 0 until sortedScoreList.size){
            if (i % m == m - 1){
                sumScore += sortedScoreList[i]
            }
        }
        return sumScore * m
    }
}