package 프로그래머스_코틀린.level2

class Solution5 {
    fun solution(s: String): String {
        var intList = s.split(" ").map{it.toInt()}
        return "${intList.minOrNull()} ${intList.maxOrNull()}"
    }
}