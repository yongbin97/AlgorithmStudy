package 프로그래머스_코틀린.level1

class Solution42 {
    fun solution(cards1: Array<String>, cards2: Array<String>, goal: Array<String>): String {
        var answer: String = "Yes"
        var cardList1 = cards1.toList()
        var cardList2 = cards2.toList()

        for (word in goal){
            if (word == cardList1.getOrNull(0)){
                if (cardList1.size > 1){
                    cardList1 = cardList1.slice(1..cardList1.size-1)
                } else{
                    cardList1 = emptyList()
                }
            } else if (word == cardList2.getOrNull(0)){
                if (cardList2.size > 1){
                    cardList2 = cardList2.slice(1..cardList2.size-1)
                } else{
                    cardList2 = emptyList()
                }
            } else {
                answer = "No"
                break
            }
        }

        return answer
    }
}