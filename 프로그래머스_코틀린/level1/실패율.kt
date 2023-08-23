package 프로그래머스_코틀린.level1


// fail
class Solution47 {
    fun solution(N: Int, stages: IntArray): IntArray {
        var answer = intArrayOf()
        var countMap = HashMap<Int, Int>()
        var failRateMap = HashMap<Int, Float>()

        stages.toList().forEach{ stage ->
            countMap[stage] = countMap.getOrDefault(stage, 0) + 1
        }
        var sum = countMap.values.sum().toFloat()
        for (i in 1 .. N){
            var current = countMap.getOrDefault(i, 0).toFloat()
            failRateMap.put(i, current / sum)
            sum -= current
        }
        failRateMap.toList().sortedByDescending {it.second}.forEach {
            answer += it.first
        }

        return answer
    }
}