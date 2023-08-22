package 프로그래머스_코틀린.level1

class Solution38 {
    fun solution(food: IntArray): String {
        var answer: String = "0"
        for (idx in food.size-1 downTo 1){
            var f = ""
            repeat(food[idx] / 2){
                f += idx.toString()
            }
            answer = f + answer + f
        }
        return answer
    }
}