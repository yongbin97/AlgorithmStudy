package 프로그래머스_코틀린.level3

class Solution5 {
    fun solution(tickets: Array<Array<String>>): Array<String> {
        var remainTickets = tickets.sortedBy{it[1]}.toList()
        return travel("ICN", remainTickets)!!.toTypedArray()
    }

    fun travel(airport: String, remainTickets: List<Array<String>>): MutableList<String>? {
        if (remainTickets.isEmpty()) return mutableListOf(airport)

        var nextTicketList = remainTickets.filter { ticket ->
            ticket.first() == airport
        }

        if (nextTicketList.isEmpty()) return null

        for (nextTicket in nextTicketList){
            var newRemainTickets = remainTickets.filter{
                it != nextTicket
            }
            println("")
            var path: MutableList<String>? = travel(nextTicket.last(), newRemainTickets)

            if (path == null) continue
            else {
                path.add(0, airport)
                return path
            }
        }
        return null
    }
}
// start = ICN
// ticket: from -> to
// 모두 갈 수 있는 방법이 2개 이상 -> 알파벳 순
// start = ICN
// ticket: from -> to
// 모두 갈 수 있는 방법이 2개 이상 -> 알파벳 순
//[["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
//[
//["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
//
//["ICN","BOO","DOO","BOO","ICN","COO","DOO","COO"]
//["ICN","BOO","DOO","BOO","ICN","COO","DOO","COO","BOO"]
