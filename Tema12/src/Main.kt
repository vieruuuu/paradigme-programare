import java.io.File
import java.util.Scanner

fun ex1() {
  val initial = listOf(1, 21, 75, 39, 7, 2, 35, 3, 31, 7, 8)
  println(initial)

  val filtered = initial.filter { it >= 5 }
  println(filtered)

  val pairs = filtered.chunked(2).map { lst -> lst[0] to lst[1] }
  println(pairs)

  val multiplied = pairs.map { it.first * it.second }
  println(multiplied)

  val summed = multiplied.sum()
  println(summed)
}

private const val alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

fun caesar(text: String, key: Int): String =
    text
        .map {
          val characterValue = alphabet.indexOf(it)

          val shiftCharacter = (characterValue + key) % alphabet.length

          alphabet[shiftCharacter]
        }
        .fold("") { acc, ch -> acc + ch }

fun ex2() {
  print("offset: ")
  val n = Scanner(System.`in`).nextInt()

  val file = File("data.txt")
  file.forEachLine { line -> println(caesar(line, n)) }
}

class TestFunctor<K, V>(val map: MutableMap<K, V>) {
  fun map(function: (K, V) -> Pair<K, V>) =
      TestFunctor(map.map { function(it.key, it.value) }.toMap(mutableMapOf()))
}

fun String.toPascalCase(): String =
    this.split(" ").joinToString(separator = "") { it.replaceFirstChar { it.uppercaseChar() } }

fun ex4() {
  val map = mutableMapOf(1 to "12", 2 to "23", 3 to "abcd", 4 to "XYZ")

  var functor = TestFunctor(map)
  functor = functor.map { k, v -> Pair(k, "Test $v") }
  functor = functor.map { k, v -> Pair(k, v.toPascalCase()) }

  println(functor.map)
}

fun main() {
  // ex1()
  // ex2()

  ex4()
}
