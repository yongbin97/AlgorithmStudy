package 프로그래머스_코틀린.level1

class Solution32 {
    fun solution(s: String, n: Int): String {
        var answer = ""
        for (c in s){
            if (c == ' '){
                answer += c
            } else{
                answer += move(c, n)
            }
        }

        return answer
    }
    fun move(c: Char, n: Int): Char {
        var targetCharCode: Int
        if (c.toInt() <= 90){
            targetCharCode = (c.toInt() + n) / 91 * 65 + (c.toInt() + n) % 91
        } else{
            targetCharCode = (c.toInt() + n) / 123 * 97 + (c.toInt() + n) % 123
        }
        return targetCharCode.toChar()
    }
}