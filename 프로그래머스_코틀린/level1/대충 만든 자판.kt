package 프로그래머스_코틀린.level1

class Solution52 {
    fun solution(keymap: Array<String>, targets: Array<String>): IntArray {
        var answer: IntArray = intArrayOf()
        var keyHashMap = HashMap<Char, Int>()
        for (keys in keymap){
            for ((idx, k) in keys.withIndex()){
                keyHashMap.put(k, minOf(keyHashMap.getOrDefault(k, 100), idx + 1))
            }
        }
        for (target in targets){
            var total = 0
            for (c in target){
                var count = keyHashMap.getOrDefault(c, -1)
                if (count == -1){
                    total = -1
                    break
                } else {
                    total += count
                }
            }
            answer += total
        }

        return answer
    }
}