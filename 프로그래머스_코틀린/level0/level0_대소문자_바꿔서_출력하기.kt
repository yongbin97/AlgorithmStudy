package 프로그래머스_코틀린.level0

fun main(args: Array<String>) {
    val s1 = readLine()!!
    for (s in s1){
        if (s.isUpperCase()){
            print(s.toLowerCase())
        }else{
            print(s.toUpperCase())
        }
    }
}