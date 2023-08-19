package 프로그래머스_코틀린.level1

class Solution17 {
    fun solution(numbers: IntArray): Int {
        var result = 0
        for (i in 0..9){
            if (!numbers.contains(i)) result += i
        }
        return result
    }
}