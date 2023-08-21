package 프로그래머스_코틀린.level1

class Solution34 {
    fun solution(strings: Array<String>, n: Int): Array<String> {
        return strings.sortedWith(compareBy({it[n]}, {it})).toTypedArray()
    }
}