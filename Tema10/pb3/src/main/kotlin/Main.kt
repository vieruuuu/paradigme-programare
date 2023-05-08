import java.util.concurrent.LinkedBlockingQueue
import kotlin.concurrent.thread
import kotlin.random.Random
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.channels.Channel.Factory.UNLIMITED

sealed class Message {
  class Number(val n: Int) : Message()
  object End : Message()
}

suspend fun gauss(c: Channel<Message>) {
  while (true) {
    val msg = c.receive()

    when (msg) {
      is Message.Number -> {
        println("[coroutine - ${msg.n}]: ${((msg.n + 1) * msg.n) / 2}")
      }
      is Message.End -> break
      else -> Thread.sleep(10)
    }
  }
}

@DelicateCoroutinesApi
fun coroutines(end: Int): Unit = runBlocking {
  val scope = CoroutineScope(newFixedThreadPoolContext(2, "pool"))

  val channel = Channel<Message>(capacity = UNLIMITED)

  val jobs = List(4) { scope.launch { gauss(channel) } }

  for (i in 0..end) {
    channel.send(Message.Number(i))
  }

  for (i in 0..4) {
    channel.send(Message.End)
  }

  jobs.forEach { it.join() }
}

fun threads(end: Int) {
  val queue = LinkedBlockingQueue<Message>()

  for (i in 0..3) {
    thread {
      var msg = queue.take()

      while (msg != null) {
        when (msg) {
          is Message.Number -> println("[thread - ${msg.n}]: ${((msg.n + 1) * msg.n) / 2}")
          is Message.End -> break
          else -> Thread.sleep(10)
        }

        msg = queue.take()
      }
    }
  }

  for (i in 0..end) {
    queue.add(Message.Number(i))
  }

  for (i in 0..4) {
    queue.add(Message.End)
  }
}

@DelicateCoroutinesApi
fun main() {
  val a = Random.nextInt()
  val nr = (a * a) % 100

  threads(nr)
  coroutines(nr)
}
