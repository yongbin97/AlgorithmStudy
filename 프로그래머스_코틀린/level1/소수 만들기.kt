package 프로그래머스_코틀린.level1

class Solution45 {
    fun solution(nums: IntArray): Int {
        var answer = 0
        for (i in 0 until nums.size-2){
            for (j in i+1 until nums.size-1){
                for (k in j+1 until nums.size){
                    var sum = nums[i] + nums[j] + nums[k]
                    if (check(sum)){
                        answer += 1
                    }
                }
            }
        }
        return answer
    }

    fun check(num: Int): Boolean{
        for (i in 2..num-1){
            if(num % i == 0){
                return false
            }
        }
        return true
    }
}