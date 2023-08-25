package 프로그래머스_코틀린.level3

import kotlin.math.*

class Solution4 {
    fun solution(begin: String, target: String, words: Array<String>): Int {
        return if (!words.contains(target)) 0 else change(begin, target, 0, words.toMutableList())
    }

    fun change(currWord: String, target: String, count: Int, wordList: MutableList<String>): Int{
        if (currWord == target) return count

        var nextWordList = wordList.filter { word ->
            word.toList().filterIndexed{idx, c ->
                c != currWord.toList()[idx]
            }.count() == 1
        }
        if (nextWordList.isEmpty()) return Int.MAX_VALUE

        var minCount = Int.MAX_VALUE
        for (nextWord in nextWordList){
            wordList.remove(nextWord)
            var count = change(nextWord, target, count+1, wordList)
            minCount = min(minCount, count)
        }
        return minCount
    }
}