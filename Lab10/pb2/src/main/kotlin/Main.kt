import java.io.*
import java.util.concurrent.atomic.AtomicInteger
import kotlin.system.*
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*

@OptIn(kotlinx.coroutines.ObsoleteCoroutinesApi::class)
fun CoroutineScope.counterActor() =
    actor<Int> {
      var contor = 0

      for (msg in channel) {
        if (msg == 0) {
          println("Contor = ${contor}")
        } else {
          contor++
        }
      }
    }

suspend fun CoroutineScope.massiveRun(action: suspend () -> Unit) {
  val n = 100
  val k = 1000
  val time = measureTimeMillis {
    val jobs = List(n) { launch { repeat(k) { action() } } }
    jobs.forEach { it.join() }
  }
  println("S-au efectuat ${n * k} operatii in $time ms")
}

val counter = AtomicInteger(0)

@DelicateCoroutinesApi
fun main() =
    runBlocking<Unit> {
      val contor = counterActor()

      GlobalScope.massiveRun { contor.send(1) }

      contor.send(0)
      contor.close()
    }
