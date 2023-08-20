package 프로그래머스_코틀린.level1

class Solution29 {
    fun solution(s: String): String {
        var result = listOf<String>()
        for (word in s.split(" ")){
            result += convert(word)
        }
        return result.joinToString(" ")
    }

    fun convert(word: String): String{
        var newWord = ""
        for ((idx, w) in word.toCharArray().withIndex()){
            if (idx % 2 == 0){
                newWord += w.toUpperCase()
            }else{
                newWord += w.toLowerCase()
            }
        }
        return newWord
    }
}