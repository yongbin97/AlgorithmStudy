package 프로그래머스_코틀린.level0

class Solution4 {
    fun solution(my_string: String, k: Int): String {
        var answer = StringBuilder()
        repeat(k){
            answer.append(my_string)
        }
        return answer.toString()
    }
}