package 프로그래머스_코틀린.level0


class Solution1 {
    fun solution(my_string: String, overwrite_string: String, s: Int): String {
        var firstRan = IntRange(0, s-1)
        var lastRan = IntRange(s+overwrite_string.length, my_string.length-1)
        return my_string.slice(firstRan) + overwrite_string + my_string.slice(lastRan)
    }
}