package 프로그래머스_코틀린.level1

class Solution16 {
    fun solution(phone_number: String): String {
        var result = StringBuilder()

        var sub = phone_number.substring(phone_number.length - 4, phone_number.length)
        for (i in 0 .. phone_number.length - 5){
            result.append("*")
        }
        result.append(sub)
        return result.toString()
    }
}