package 프로그래머스_코틀린.level1


class Solution15 {
    fun solution(absolutes: IntArray, signs: BooleanArray): Int {
        var answer: Int = 0

        for ((it, abs) in absolutes.withIndex()){
            if (signs[it]){
                answer += abs
            }else{
                answer -= abs
            }
        }

        return answer
    }
}