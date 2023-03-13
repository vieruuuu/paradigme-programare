package com.vieru.tema3

import org.jsoup.Jsoup

fun main(args: Array<String>) {
  val document = Jsoup.connect("https://feeds.simplecast.com/54nAGcIl").get()

  val docTitle = document.select("title")[0]!!.text()
  val docLink = document.select("link")[0]!!.text()
  val docDescription = document.select("description")[0]!!.text()

  println("$docTitle ($docLink) \n\n\n\t$docDescription\n\n\n\n")

  document
      .select("item")
      .forEach({
        val title = it.select("title").text()
        val link = it.select("link").text()
        val description = it.select("description").text()
        val pubDate = it.select("pubDate").text()

        println("$title [$pubDate] ($link)\n\n\n\t$description\n\n\n\n")
      })
}
