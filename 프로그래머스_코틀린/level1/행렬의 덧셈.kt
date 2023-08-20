package 프로그래머스_코틀린.level1

class Solution26 {
    fun solution(arr1: Array<IntArray>, arr2: Array<IntArray>): Array<IntArray> {
        var answer = arrayOf<IntArray>()
        for ((i, arr) in arr1.withIndex()){
            var intArr = intArrayOf()
            for ((j, value) in arr.withIndex()){
                intArr += value + arr2[i][j]
            }
            answer += intArr
        }

        return answer
    }
}