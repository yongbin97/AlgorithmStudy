package 프로그래머스_코틀린.level3

import java.util.*

class Solution7 {
    fun solution(operations: Array<String>): IntArray {
        var answer = intArrayOf()
        var pq = PriorityQueue<Int>(Collections.reverseOrder())
        var pqReversed = PriorityQueue<Int>()

        for (operation in operations){
            if (operation.split(" ")[0] == "I"){
                pq.add(operation.split(" ")[1].toInt())
                pqReversed.add(operation.split(" ")[1].toInt())
            } else{
                if (pq.isEmpty()) continue
                when(operation.split(" ")[1].toInt()){
                    1 -> pqReversed.remove(pq.poll())
                    -1 -> pq.remove(pqReversed.poll())
                    else -> continue
                }
            }
        }
        if (pq.isEmpty()){
            answer += intArrayOf(0,0)
        } else{
            answer += pq.poll()
            answer += pqReversed.poll()
        }

        return answer
    }
}