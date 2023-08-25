package 프로그래머스_코틀린.level1

class Solution53 {
    fun solution(s: String, skip: String, index: Int): String {
        var answer: String = ""
        val skipList = skip.toList().map{it.toInt()}
        for (c in s){
            var target = c.toInt()
            for (i in 0 until index){
                target = (target - 96) % 26 + 97
                while(skipList.contains(target)){
                    target = (target - 96) % 26 + 97
                }
            }
            answer += target.toChar()
        }
        return answer
    }
}