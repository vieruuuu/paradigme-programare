package com.vieru.tema3

import java.io.File

@OptIn(kotlin.ExperimentalStdlibApi::class)
fun main(args: Array<String>) {
  File("ebook.txt")
      .readLines()
      .map { it.replace(Regex("\\s+"), " ").trim() }
      .filter { it.isNotEmpty() && !Regex("\\d+").matchesAt(it, 1) }
      .forEach({ println(it) })
}
