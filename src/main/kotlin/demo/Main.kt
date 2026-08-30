package demo

fun describe(n: Int): String = if (n > 0) "positive" else "non-positive"

fun main() {
    println(describe(1))
}
