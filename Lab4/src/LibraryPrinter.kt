class LibraryPrinter {
  companion object {
    fun printBooksRaw(books: Set<Book>) {
      books.forEach({ println(it) })
    }

    fun printHTML(books: Set<Book>) {
      println("<div>")

      books.forEach({
        println("\t<div>")
        println("\t\t<h2>Cartea: ${it.getName()}</h2>")
        println("\t\t<h5>Scrisa de: ${it.getAuthor()}</h5>")
        println("\t\t<h5>Publicata de: ${it.getPublisher()}</h5>")
        println("\t\t<h5>------------- Continut -------------</h5>")
        println("\t\t<pre>${it.getContent()}</pre>\"")
        println("\t\t<h5>-------- Terminare-Continut --------</h5>")
        println("\t<div>")
      })

      println("</div>")
    }

    fun printJSON(books: Set<Book>) {
      println("[")

      books.forEach({
        println("\t{")
        println("\t\t\"name\": \"${it.getName()}\"")
        println("\t\t\"author\": \"${it.getAuthor()}\"")
        println("\t\t\"publisher\": \"${it.getPublisher()}\"")
        println("\t\t\"text\": \"${it.getContent()}\"")
        println("\t},")
      })

      println("]")
    }
  }
}
