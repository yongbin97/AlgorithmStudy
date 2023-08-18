package 프로그래머스_코틀린

fun main(args: Array<String>) {
    val (a, b) = readLine()!!.split(' ').map(String::toInt)
    print("${a} + ${b} = ${a+b}")
}