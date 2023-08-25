package 프로그래머스_코틀린.level3

class Solution {
    fun solution(jobs: Array<IntArray>): Int {
        var answer = 0
        var time = 0
        var readyQueue = jobs.toMutableList()
        while (readyQueue.size > 0){

            var currentJobList = readyQueue.filter { it ->
                it.first() <= time
            }.sortedBy{it.last()}

            if (currentJobList.isEmpty()){
                time ++
                continue
            } else {
                time += currentJobList.first()[1]
                answer += time - currentJobList.first()[0]
                readyQueue.remove(currentJobList.first())
            }
        }

        return answer / jobs.size
    }
}
