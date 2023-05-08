import java.util.concurrent.*
import kotlin.concurrent.thread
import kotlin.random.Random
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.channels.Channel.Factory.UNLIMITED
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking

sealed class Message {
  class Number(val n: Int) : Message()
  object End : Message()
}

fun processWithThreads(list: List<Int>, alpha: Int) {
  val msgQ = LinkedBlockingQueue<Message>()

  thread(name = "multiplication thread") {
    for (n in list) {
      msgQ.put(Message.Number(n * alpha))
    }

    msgQ.put(Message.End)
  }

  val sortedQ = LinkedBlockingQueue<List<Int>>()

  thread() {
    val unsortedList = mutableListOf<Int>()

    var message = msgQ.take()

    while (message != null) {
      when (message) {
        is Message.Number -> unsortedList.add(message.n)
        is Message.End -> break
        else -> Thread.sleep(10)
      }

      message = msgQ.take()
    }

    sortedQ.add(unsortedList.sorted().toList())
  }

  thread() { println(sortedQ.take()) }
}

fun processWithCoroutines(list: List<Int>, alpha: Int) = runBlocking {
  val messageQueue = Channel<Message>(UNLIMITED)
  val sortedQueue = Channel<List<Int>>(1)

  launch {
    for (elem in list) {
      messageQueue.send(Message.Number(elem * alpha))
    }

    messageQueue.send(Message.End)
  }

  launch {
    val multipliedNumbers = mutableListOf<Int>()
    for (msg in messageQueue) {
      when (msg) {
        is Message.Number -> multipliedNumbers.add(msg.n)
        is Message.End -> break
        else -> Thread.sleep(10)
      }
    }

    sortedQueue.send(multipliedNumbers.sorted().toList())
  }

  launch {
    val sortedNumbers = sortedQueue.receive()
    println(sortedNumbers)
  }
}

fun main() {
  val list = List(100) { Random.nextInt() }
  val alpha = Random.nextInt()

  processWithThreads(list, alpha)
  processWithCoroutines(list, alpha)
}
