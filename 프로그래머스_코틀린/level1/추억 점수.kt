package 프로그래머스_코틀린.level1

class Solution40 {
    fun solution(name: Array<String>, yearning: IntArray, photo: Array<Array<String>>): IntArray {
        var answer: IntArray = intArrayOf()
        var yearningMap = name.toList().zip(yearning.toList()).toMap()

        for (nameList in photo){
            var sum = 0
            for (name in nameList){
                sum += yearningMap.getOrDefault(name, 0)
            }
            answer += sum
        }
        return answer
    }
}