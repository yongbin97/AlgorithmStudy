package 프로그래머스_코틀린.level2

class Solution2 {
    fun solution(s: String): String {
        var answer = ""
        var flag = false
        for (char in s){
            if (char == ' '){
                flag = false
                answer += char
            } else{
                if (flag){
                    answer += char.toLowerCase()
                } else{
                    answer += char.toUpperCase()
                    flag = true
                }
            }
        }
        return answer
    }
}