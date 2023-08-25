package 프로그래머스_코틀린.level1

class Solution55 {
    fun solution(s: String): Int {
        var answer: Int = 0
        var sameCount = 0
        var diffCount = 0
        var x: Char? = s.first()

        for (c in s) {
            if (x == null) x = c
            if (c == x)sameCount ++
            else diffCount ++

            if (sameCount == diffCount){
                answer ++
                x = null
                sameCount = 0
                diffCount = 0
            }
        }
        if (sameCount != diffCount) answer ++
        return answer
    }
}