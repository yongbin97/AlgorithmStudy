package 프로그래머스_코틀린.level1

fun main(args: Array<String>) {
    val (a, b) = readLine()!!.split(' ').map(String::toInt)
    repeat(b){
        repeat(a){
            print("*")
        }
        println()
    }
}