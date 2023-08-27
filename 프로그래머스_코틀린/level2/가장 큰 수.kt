package 프로그래머스_코틀린.level2

class Solution3 {
    fun solution(numbers: IntArray): String {
        var stringList = numbers
            .sortedWith { a, b ->
                "$a$b".compareTo("$b$a")
            }.reversed()
        return if (stringList.first() == 0) "0"
        else stringList.joinToString("")
    }
}