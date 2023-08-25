package 프로그래머스_코틀린.level2

import kotlin.math.*


class Solution60 {
    fun solution(k: Int, dungeons: Array<IntArray>): Int {
        var answer: Int = -1
        var dungeonList = dungeons.toList()

        return explore(k, 0, dungeonList)
    }

    fun explore(k: Int, count: Int, dungeonList: List<IntArray>): Int{
        if (dungeonList.size == 0) return count

        var maxCount = count
        for ((idx, dungeon) in dungeonList.withIndex()){
            if (k >= dungeon[0]){
                var c = explore(k - dungeon[1], count+1, dungeonList.filterIndexed{i, dugeon -> i != idx})
                maxCount = max(maxCount, c)
            }
        }
        return maxCount
    }
}

// [최소 피로도, 소모 피로도]
// 1 <= 소모 <= 최소 <= 1000