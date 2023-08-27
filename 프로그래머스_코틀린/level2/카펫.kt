package 프로그래머스_코틀린.level2

class Solution6 {
    fun solution(brown: Int, yellow: Int): IntArray {
        var sum = brown / 2 + 2
        var multiply = yellow - 4 + 2 * sum

        for (i in 1..sum/2){
            if (i * (sum-i) == multiply){
                return intArrayOf(sum-i, i)
            }
        }
        return intArrayOf()
    }
}

//(a, b) (a>=b)
//brown = (a + b - 2) * 2
//yellow = (a-2) * (b-2)
//       = ab -2 (a+b) + 4
