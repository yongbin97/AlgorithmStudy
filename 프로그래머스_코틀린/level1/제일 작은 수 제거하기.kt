package 프로그래머스_코틀린.level1

class Solution18 {
    fun solution(arr: IntArray): IntArray {
        var arrayList = arr.toTypedArray().toMutableList()
        var minValue = arr.first()
        var minIdx = 0

        for ((idx, value) in arrayList.withIndex()){
            if (minValue > value){
                minValue = value
                minIdx = idx
            }
        }
        arrayList.removeAt(minIdx)
        return if (arrayList.isEmpty()) intArrayOf(-1) else arrayList.toIntArray()

    }
}