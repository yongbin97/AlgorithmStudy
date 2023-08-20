package 프로그래머스_코틀린.level1

class Solution25 {
    fun solution(s: String): Boolean {
        var length = s.filter{!it.isDigit()}.length
        return (s.length == 4 || s.length == 6) && length == 0
    }
}