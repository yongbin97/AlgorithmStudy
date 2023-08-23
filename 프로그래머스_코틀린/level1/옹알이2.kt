package 프로그래머스_코틀린.level1

class Solution49 {
    fun solution(babbling: Array<String>): Int {
        var answer: Int = 0
        var letters = hashMapOf("aya" to "1", "ye" to "2", "woo" to "3", "ma" to "4")
        for (b in babbling){
            var baby = b
            for ((l, idx) in letters){
                baby = baby.replace(l, idx)
            }
            if (baby.toIntOrNull() != null){
                if(!("11" in baby || "22" in baby || "33" in baby || "44" in baby)){
                    answer += 1
                }
            }
        }

        return answer
    }
}