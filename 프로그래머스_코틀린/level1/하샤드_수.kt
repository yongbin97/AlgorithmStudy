package 프로그래머스_코틀린.level1

class Solution10 {
    fun solution(x: Int): Boolean {
        var sum = 0
        for (i in x.toString()){
            sum += i - '0'
        }

        return x % sum == 0
    }
}