package 프로그래머스_코틀린.level3

class Solution1 {
    var computerList = mutableListOf<Int>()


    fun solution(n: Int, computers: Array<IntArray>): Int {
        var answer = 0
        for (i in 0 until n) computerList += i

        while(computerList.size > 0){
            answer ++
            search(n, computers, computerList.removeAt(0))
        }

        return answer
    }

    fun search(n: Int, computers: Array<IntArray>, computer: Int){
        for (i in 0 until n){
            if(computerList.contains(i) && computers[computer][i] == 1){
                computerList.remove(i)
                search(n, computers, i)
            }
        }
    }
}