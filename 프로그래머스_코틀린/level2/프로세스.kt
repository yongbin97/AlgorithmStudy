package 프로그래머스_코틀린.level2

import kotlin.collections.ArrayDeque

class Solution56 {
    fun solution(priorities: IntArray, location: Int): Int {
        var answer = 0
        var queue = ArrayDeque<Pair<Int, Int>>()
        for ((idx, p) in priorities.withIndex()){
            queue.add(Pair(idx, p))
        }

        while (queue.size > 0){
            var firstEle = queue.removeFirst()
            if (queue.any { it.second > firstEle.second }){
                queue.add(firstEle)
            } else{
                answer ++
                if (location == firstEle.first) break
            }
        }
        return answer
    }
}
