package 프로그래머스_코틀린.level0

import kotlin.math.*

class Solution6 {
    fun solution(a: Int, b: Int): Int {
        var ab = "$a$b".toInt()
        var ab2 = 2 * a * b

        return max(ab, ab2)
    }
}