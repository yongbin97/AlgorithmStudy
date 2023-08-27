package 프로그래머스_코틀린.level2

class Solution10 {
    fun solution(clothes: Array<Array<String>>): Int {
        var clothMap = HashMap<String, Int>()
        for (cloth in clothes){
            if (clothMap.containsKey(cloth[1])){
                clothMap[cloth[1]] = clothMap[cloth[1]]!! + 1
            } else{
                clothMap[cloth[1]] = 1
            }
        }
        var result = 1
        for ((key, item) in clothMap){
            result *= (item + 1)
        }
        return result - 1
    }

    fun solution2(clothes: Array<Array<String>>) = clothes
        .groupBy { it[1] }.values   // group by type of clothes, keep only names of clothes
        .map { it.size + 1 }        // number of things to wear in a group (including wearing nothing)
        .reduce(Int::times)         // combine
        .minus(1)
}