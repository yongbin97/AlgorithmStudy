package 프로그래머스_코틀린.level1

class Solution31 {
    fun solution(sizes: Array<IntArray>): Int {
        var big = 0
        var small = 0

        for (size in sizes){
            var min: Int = size.minOrNull()!!.toInt()
            var max: Int = size.maxOrNull()!!.toInt()
            if (max > big){
                big = max
            }
            if (min > small){
                small = min
            }
        }
        return big * small
    }
}