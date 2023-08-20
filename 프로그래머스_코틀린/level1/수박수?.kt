package 프로그래머스_코틀린.level1

class Solution20 {
    fun solution(n: Int): String {
        var result = ""
        repeat(n){
            if (it%2==0){
                result += "수"
            }else{
                result += "박"
            }
        }
        return result
    }
}