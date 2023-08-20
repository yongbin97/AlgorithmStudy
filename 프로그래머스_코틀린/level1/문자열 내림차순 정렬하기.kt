package 프로그래머스_코틀린.level1

class Solution23 {
    fun solution(s: String): String {
        return s.toCharArray().sortedArrayDescending().joinToString("")
    }
}