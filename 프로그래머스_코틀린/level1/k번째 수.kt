package 프로그래머스_코틀린.level1

class Solution35 {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        var answer = intArrayOf()
        for (command in commands){
            answer += getNum(array, command)
        }
        return answer
    }

    fun getNum(array: IntArray, command: IntArray): Int {
        var slicedArray = array.slice(command[0]-1..command[1]-1).sorted()
        return slicedArray[command[2]-1]
    }
}