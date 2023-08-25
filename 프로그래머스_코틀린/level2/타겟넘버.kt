package 프로그래머스_코틀린.level2

class Solution61 {
    fun solution(numbers: IntArray, target: Int): Int {
        var answer = calculation(target, 0, 0, numbers.toList())
        return answer
    }

    fun calculation(target: Int, count:Int, sum: Int, numberList: List<Int>): Int{
        if (numberList.isEmpty()){
            if (sum == target) return count + 1
            else return count
        }

        var num = numberList.first()

        var plus = calculation(target, count, sum+num, numberList.slice(1..numberList.size-1))
        var minus = calculation(target, count, sum-num, numberList.slice(1..numberList.size-1))

        return plus + minus
    }
}