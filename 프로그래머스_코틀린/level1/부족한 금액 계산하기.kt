package 프로그래머스_코틀린.level1

class Solution24 {
    fun solution(price: Int, money: Int, count: Int): Long {
        var n: Long = (1L + count) * count / 2L
        var change: Long = price * n - money.toLong()
        return if (change > 0L) change else 0L
    }
}