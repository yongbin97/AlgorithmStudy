package 프로그래머스_코틀린.level0

class Solution2 {
    fun solution(str1: String, str2: String): String {
        var answer = StringBuilder()

        repeat(str1.length){
            answer.append(str1[it])
            answer.append(str2[it])
        }

        return answer.toString()
    }
}