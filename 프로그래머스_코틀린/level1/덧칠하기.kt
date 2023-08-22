package 프로그래머스_코틀린.level1

class Solution46 {
    fun solution(n: Int, m: Int, section: IntArray): Int {
        var answer: Int = 0
        var sectionList = section.toMutableList()
        while (sectionList.size > 0){
            var start = sectionList.first()
            var last = start + m
            sectionList.removeIf{ it >= start && it < last}
            answer += 1
        }
        return answer
    }
}