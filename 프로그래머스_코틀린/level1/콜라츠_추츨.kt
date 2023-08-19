package 프로그래머스_코틀린.level1

class Solution12 {
    fun solution(num: Int): Int {
        var answer = 0
        var number = num

        while (number != 1 && answer < 500){
            if (number % 2 == 0){
                number = number / 2
            }else{
                number = number * 3 + 1
            }
            answer += 1
        }

        return if (answer == 500) -1 else answer
    }
}

// 꼬리재귀
//class Solution {
//    fun solution(num: Int): Int = collatzAlgorithm(num.toLong(),0)
//
//    tailrec fun collatzAlgorithm(n:Long, c:Int):Int =
//        when{
//            c > 500 -> -1
//            n == 1L -> c
//            else -> collatzAlgorithm(if( n%2 == 0L ) n/2 else (n*3)+1, c+1)
//        }
//}
