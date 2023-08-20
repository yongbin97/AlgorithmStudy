package 프로그래머스_코틀린.level1

class Solution27 {
    fun solution(n: Int, m: Int): IntArray {
        var gcdNM = gcd(n, m)
        var lcmNM = ((n * m).toLong() / gcdNM.toLong()).toInt()
        var answer = intArrayOf(gcdNM, lcmNM)
        return answer
    }

    fun gcd(a: Int, b: Int): Int {
        return if (b==0) a else gcd(b, a%b)
    }
}