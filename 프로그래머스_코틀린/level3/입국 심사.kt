package 프로그래머스_코틀린.level3


class Solution2 {
    fun solution(n: Int, times: IntArray): Long {
        var answer: Long = 0

        var min: Long = n.toLong()/times.size.toLong() * times.minOrNull()!!.toLong()
        var max: Long = n.toLong() * times.maxOrNull()!!.toLong()

        while(min <= max){
            var mid = (min + max)/2

            var sum: Long = 0
            times.forEach{ sum += mid/it }

            if (sum >= n) max = mid - 1
            else min = mid + 1
        }

        return max + 1
    }

}