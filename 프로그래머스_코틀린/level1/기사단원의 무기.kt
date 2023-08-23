package 프로그래머스_코틀린.level1

class Solution48 {
    fun solution(number: Int, limit: Int, power: Int): Int {
        var answer: Int = 0
        for (num in 1..number){
            var count = getPower(num)
            when (count > limit){
                true -> answer += power
                else -> answer += count
            }
        }
        return answer
    }

    fun getPower(number: Int): Int{
        var power = 0
        var i = 1
        while (i * i <= number){
            if (i * i == number) power += 1
            else if (number % i == 0) power += 2
            i ++
        }
        return power
    }
}