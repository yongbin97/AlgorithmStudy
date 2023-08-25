package 프로그래머스_코틀린.level1

class Solution54 {
    fun solution(board: Array<IntArray>, moves: IntArray): Int {
        var answer = 0
        val boardMap = (1..board.size).associateWith { mutableListOf<Int>() }
        val basket = mutableListOf<Int>()

        for (layer in board){
            for ((x, item) in layer.withIndex()){
                boardMap.getOrDefault(x + 1, mutableListOf<Int>()).add(item)
            }
        }
        for (i in moves){
            val col: MutableList<Int>? = boardMap[i]
            if (col != null){
                for ((idx, item) in col.withIndex()){
                    if (item != 0){
                        col[idx] = 0
                        if (basket.isNotEmpty() && basket.last() == item){
                            answer += 2
                            basket.remove(item)
                        } else {
                            basket.add(item)
                        }
                        break
                    }
                }
            }
        }
        return answer
    }
}

// 바구니 - stack => stack.last() == curr => stack.remove(-1) *count ++
// board -> 뽑으면 0
