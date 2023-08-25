package 프로그래머스_코틀린.level1

class Solution50{
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        var lostList = lost.sorted().toMutableList()
        val reserveList = reserve.sortedByDescending{it}.toMutableList()

        for (r in reserve.sortedByDescending{it}){
            if (lostList.contains(r)){
                lostList.remove(r)
                reserveList.remove(r)
            }
        }
        for (r in reserveList){
            if (lostList.contains(r + 1)){
                lostList.remove(r + 1)
            } else if (lostList.contains(r - 1)){
                lostList.remove(r - 1)
            }
        }
        return n - lostList.size
    }
}