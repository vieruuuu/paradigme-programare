class Book(private val data: Content) {

  override fun toString(): String {
    return arrayOf(
            "Cartea: ${this.getName()}",
            "Scrisa de: ${this.getAuthor()}",
            "Publicata de: ${this.getPublisher()}",
            "------------- Continut -------------",
            this.getContent(),
            "-------- Terminare-Continut --------",
        )
        .joinToString("\n")
  }

  fun getName(): String {
    return data.getName()
  }
  fun getAuthor(): String {
    return data.getAuthor()
  }
  fun getPublisher(): String {
    return data.getPublisher()
  }
  fun getContent(): String {
    return data.getText()
  }

  fun hasAuthor(author: String): Boolean {
    return this.getAuthor() == author
  }
  fun hasTitle(title: String): Boolean {
    return this.getName() == title
  }
  fun isPublishedBy(publisher: String): Boolean {
    return this.getPublisher() == publisher
  }
}
