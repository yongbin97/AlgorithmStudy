package 프로그래머스_코틀린.level1

import kotlin.math.*

class Solution8 {
    fun solution(n: Long): Long {
        var root = sqrt(n.toDouble()).toLong()

        return if (root * root == n) return (root + 1) * (root + 1) else -1
    }
}