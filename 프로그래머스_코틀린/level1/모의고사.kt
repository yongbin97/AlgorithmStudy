package 프로그래머스_코틀린.level1

class Solution44 {
    fun solution(answers: IntArray): IntArray {
        var answerCountMap = hashMapOf(1 to 0, 2 to 0, 3 to 0)

        for ((idx, answ) in answers.withIndex()){
            if (answ == get1Answer(idx)){
                answerCountMap[1] = answerCountMap.getOrDefault(1, 0) + 1
            }
            if (answ == get2Answer(idx)){
                answerCountMap[2] = answerCountMap.getOrDefault(2, 0) + 1
            }
            if (answ == get3Answer(idx)){
                answerCountMap[3] = answerCountMap.getOrDefault(3, 0) + 1
            }
        }
        var maxValue = answerCountMap.values.maxOrNull()
        return answerCountMap.filter { it.value == maxValue}.keys.toList().toIntArray()
    }

    fun get1Answer(idx: Int): Int{
        return idx % 5 + 1
    }
    fun get2Answer(idx: Int): Int {
        if (idx%2 == 0){
            return 2
        } else {
            return when(idx % 8){
                1 -> 1
                3 -> 3
                5 -> 4
                7 -> 5
                else -> 0
            }
        }
    }
    fun get3Answer(idx: Int): Int{
        return when(idx%10){
            0, 1 -> 3
            2, 3 -> 1
            4, 5 -> 2
            6, 7 -> 4
            else -> 5
        }
    }
}