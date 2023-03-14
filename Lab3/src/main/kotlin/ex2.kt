package com.vieru.lab3

import java.io.File
import java.util.*

fun updateDictionaryFromScanner(dictionary: HashMap<String, String>, input: Scanner) {
  try {
    var line = input.nextLine()
    while (line.length >= 3) {
      val words = line.split('=')
      dictionary[words[0]] = words[1]
      line = input.nextLine()
    }
  } catch (except: java.lang.Exception) {
    //
  }
}

fun main(args: Array<String>) {
  val dictionar =
      hashMapOf<String, String>(
          "Once" to "Odata",
          "upon" to "ca",
          "a" to "",
          "time" to "niciodata",
          "there" to "acolo",
          "was" to "a fost",
          "an" to "o",
          "old" to "batrana",
          "woman" to "femeie",
          "who" to "care",
          "loved" to "iubea",
          "baking" to "sa gateasca",
          "gingerbread" to "turta dulce",
          "She" to "Ea",
          "would" to "ar fi",
          "bake" to "gatit",
          "gingerbread" to "turta dulce",
          "cookies" to "biscuiti",
          "cakes" to "prajituri",
          "houses" to "case",
          "and" to "si",
          "people" to "oameni",
          "all" to "toti",
          "decorated" to "decorati",
          "with" to "cu",
          "chocolate" to "ciocolata",
          "peppermint" to "menta",
          "caramel" to "caramel",
          "candies" to "bomboane",
          "colored" to "colorate",
          "ingredients" to "ingrediente"
      )

  print("Doriti sa adaugati cuvinte noi in dictionar? [y/f/N] ")

  var stdin = Scanner(System.`in`)
  val choice = stdin.nextLine().getOrElse(0) { _ -> 'n' }.lowercase()

  if (choice == "y") {
    println(
        "Inserati cuvintele si o linie goala cand ati terminat (separati cuvantul netradus de cunvatul tradus cu =): "
    )
    updateDictionaryFromScanner(dictionar, stdin)
  } else if (choice == "f") {
    print("Introduceti calea catre fisier: ")
    val path = stdin.next()
    updateDictionaryFromScanner(dictionar, Scanner(File(path)))
  }

  val poveste =
      "Once upon a time there was an old woman who loved baking gingerbread. She would bake gingerbread cookies, cakes, houses and gingerbread people, all decorated with chocolate and peppermint, caramel candies and colored ingredients."

  val cuvintePoveste = poveste.split(" ")
  println("Cuvintele din poveste [${cuvintePoveste.count()}]:")

  println(poveste)

  println("\n")
  println("Povestea tradusa ar suna cam asa:")

  val fisier = File("poveste.txt")

  for (cuv in cuvintePoveste.map { it.trim(',', '.') }) {
    if (dictionar.contains(cuv)) {
      print(dictionar[cuv])
      fisier.writeText(dictionar[cuv]!!)
    } else {
      print("NU POATE FI TRADUS -> $cuv")
      fisier.writeText("NU POATE FI TRADUS -> $cuv")
    }

    print(" ")
    fisier.writeText(" ")
  }
}
