package 프로그래머스_코틀린.level1

class Solution37 {
    fun solution(numbers: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        for (i in 0 until numbers.size -1){
            for (j in i + 1 until numbers.size){
                answer += numbers[i] + numbers[j]
            }
        }
        answer = answer.distinct().sorted().toIntArray()
        return answer
    }
}