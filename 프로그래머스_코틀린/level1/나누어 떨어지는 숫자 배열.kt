package 프로그래머스_코틀린.level1

class Solution14 {
    fun solution(arr: IntArray, divisor: Int): IntArray {
        var result = arr.filter{it%divisor == 0}.sorted()

        if (result.isEmpty()){
            result = listOf(-1)
        }
        return result.toIntArray()
    }
}