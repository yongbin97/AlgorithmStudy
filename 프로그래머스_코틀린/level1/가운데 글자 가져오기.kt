package 프로그래머스_코틀린.level1

class Solution19 {
    fun solution(s: String): String {
        var length = s.length

        if (length % 2 == 0){
            print(length/2 - 1)
            return s.substring(length/2 - 1, length/2 + 1)
        }else{
            return s[(length-1)/2].toString()
        }

    }
}