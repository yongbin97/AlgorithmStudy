package 프로그래머스_코틀린.level1

class Solution {
    fun solution(x: Int, n: Int): LongArray {
        var answer = LongArray(n)
        var num = x.toLong()
        repeat(n){
            answer[it] = num
            num += x.toLong()
        }
        return answer
    }

//    fun solution(x: Int, n: Int): LongArray = LongArray(n) { x.toLong() * (it + 1) }

}