package 프로그래머스_코틀린.level1

class Solution36 {
    fun solution(s: String): IntArray {
        var answer: IntArray = intArrayOf()
        var charMap = HashMap<Char, Int>()
        for ((idx, c) in s.withIndex()){
            if (charMap.containsKey(c)){
                answer += idx - charMap[c]!!
            } else{
                answer += -1
            }
            charMap.put(c, idx)

        }
        return answer
    }
}