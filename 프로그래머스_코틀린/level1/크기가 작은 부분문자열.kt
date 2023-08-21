package 프로그래머스_코틀린.level1

class Solution30 {
    fun solution(t: String, p: String): Int {
        var answer: Int = 0

        for (i in 0 .. t.length - p.length){
            if(t.slice(i until i+p.length).toLong() <= p.toLong()){
                answer ++
            }

        }
        return answer
    }
}