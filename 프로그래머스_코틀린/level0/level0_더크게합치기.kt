package 프로그래머스_코틀린.level0

class Solution5 {
    fun solution(a: Int, b: Int): Int {
        var answer: Int = 0

        var aFirst = "$a$b".toInt()
        var bFirst = "$b$a".toInt()

        if (aFirst >= bFirst){
            answer = aFirst
        } else{
            answer = bFirst
        }

        return answer
    }
}