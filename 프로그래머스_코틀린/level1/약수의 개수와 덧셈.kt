package 프로그래머스_코틀린.level1

import kotlin.math.*


class Solution22 {
    fun solution(left: Int, right: Int): Int {
        var result = 0
                for (i in left .. right ){
                    var sqrtInt = sqrt(i.toDouble()).toInt()
                    if (sqrtInt * sqrtInt == i){
                        result -= i
                    } else{
                        result += i
                    }
                }
        return result
    }
}