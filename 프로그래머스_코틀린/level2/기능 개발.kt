package 프로그래머스_코틀린.level2

class Solution55 {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        var answer = intArrayOf()
        var days = listOf<Int>()

        for (i in progresses.indices){
            var remain = 100 - progresses[i]
            if (remain % speeds[i] == 0){
                days += remain / speeds[i]
            } else {
                days += remain / speeds[i] + 1
            }
        }
        var x = days.first()
        var count = 0
        for (day in days){
            if (day > x){
                answer += count
                count = 1
                x = day
            } else {
                count ++
            }
        }
        if (count != 0) answer += count
        return answer
    }
}
// 남은 진도율 = 100 - progress
// 배포 가능한 날짜 = 남은 진도율 / speed
// [5, 10, 1, 1,  20, 1] =>