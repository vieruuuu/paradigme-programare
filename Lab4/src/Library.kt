class Library(private val books: MutableSet<Book>) {
  fun getBooks(): MutableSet<Book> {
    return this.books
  }
  fun addBooks(book: Book) {
    this.books.add(book)
  }

  fun findAllByAuthor(author: String): Set<Book> {
    return this.getBooks().filter { it.hasAuthor(author) }.toSet()
  }
  fun findAllByName(name: String): Set<Book> {
    return this.getBooks().filter { it.hasTitle(name) }.toSet()
  }
  fun findAllByPublisher(publisher: String): Set<Book> {
    return this.getBooks().filter { it.isPublishedBy(publisher) }.toSet()
  }
}
