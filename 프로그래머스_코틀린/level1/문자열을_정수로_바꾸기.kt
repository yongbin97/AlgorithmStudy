package 프로그래머스_코틀린.level1

class Solution7 {
    fun solution(s: String): Int {
        var sInt = s.toIntOrNull()
        if (sInt == null){
            var prefix = s[0]
            var value = s.substring(1).toInt()
            print(prefix)
            return if (prefix.equals("-")) -1 * value else value
        } else{
            return sInt
        }
    }
}