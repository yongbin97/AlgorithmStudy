package 프로그래머스_코틀린.level1

class Solution33 {
    fun solution(s: String): Int {
        var str = s
        var digitMap = hashMapOf<String, String>(
            "zero" to "0",
            "one" to "1",
            "two" to "2",
            "three" to "3",
            "four" to "4",
            "five" to "5",
            "six" to "6",
            "seven" to "7",
            "eight" to "8",
            "nine" to "9"
        )
        for ((key, item) in digitMap){
            str = str.replace(key, item)
        }
        return str.toInt()
    }
}