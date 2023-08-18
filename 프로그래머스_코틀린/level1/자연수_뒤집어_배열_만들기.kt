package 프로그래머스_코틀린.level1

class Solution6 {
    fun solution(n: Long): IntArray {
        var n_str = n.toString()
        var result = IntArray(n_str.length)

        for ((i, s) in n_str.reversed().withIndex()){
            result[i] = s - '0'
        }
        return result
    }
}