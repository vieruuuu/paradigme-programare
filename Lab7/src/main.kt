import java.io.*

fun main() {
  val syslog = File("./syslog")
  val onlyPID = "1"

  val logSeq =
      syslog
          .readText()
          .splitToSequence("\n")
          .map {
            val recordObj = SyslogRecord(it)

            recordObj.applicationName to recordObj
          }
          .filter { it.first == onlyPID }
          .sortedBy { it.second.logEntry }
          .forEach({ println(it.second.logEntry) })
}
