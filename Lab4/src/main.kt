fun main() {
  val a =
      Library(
          mutableSetOf(
              Book(Content("author1", "text1", "name1", "publisher1", 5.6)),
              Book(Content("author2", "text2", "name2", "publisher2", 5.6)),
              Book(Content("author2", "tex3", "name3", "publisher3", 5.6))
          )
      )

  LibraryPrinter.printBooksRaw(a.getBooks())
  LibraryPrinter.printHTML(a.getBooks())
  LibraryPrinter.printJSON(a.getBooks())
}
