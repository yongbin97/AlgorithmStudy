package 프로그래머스_코틀린.level1

class Solution41 {
    fun solution(k: Int, score: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        var honor: IntArray = intArrayOf()
        for (s in score){
            honor += s
            honor = honor.sortedArrayDescending()
            if (honor.size >= k){
                answer += honor[k-1]
            } else{
                answer += honor.last()
            }
        }
        return answer
    }
}