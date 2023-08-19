package 프로그래머스_코틀린.level1

class Solution9 {
    fun solution(n: Long): Long {
        //sorted().reversed() => sortedArrayDescending()
        return n.toString().toCharArray().sorted().reversed().joinToString("") .toLong()
    }
}