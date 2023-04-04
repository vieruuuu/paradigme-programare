class SyslogRecord(val logLine: String) {
  public var timestamp: String
  public var hostname: String
  public var applicationName: String = ""
  public var pid: String = ""
  public var logEntry: String = ""

  init {
    this.timestamp = logLine.slice(IntRange(0, 14))

    val afterTimestamp = logLine.slice(IntRange(16, logLine.length - 1))

    val hostnameEnd = afterTimestamp.indexOf(" ")

    this.hostname = afterTimestamp.slice(IntRange(0, hostnameEnd))

    val afterHostname = afterTimestamp.slice(IntRange(hostnameEnd, afterTimestamp.length - 1))

    val aplicationAndPidEnd = afterHostname.indexOf(": ")

    val aplicationAndPid = afterHostname.slice(IntRange(0, aplicationAndPidEnd - 1))

    val pidStart = aplicationAndPid.indexOf("[")
    val pidEnd = aplicationAndPid.indexOf("]")

    if (pidStart == -1 || pidEnd == -1) {
      this.applicationName = aplicationAndPid
    } else {
      this.pid = aplicationAndPid.slice(IntRange(pidStart + 1, pidEnd - 1))
      this.applicationName = aplicationAndPid.slice(IntRange(0, pidStart - 1))
    }

    this.logEntry = afterHostname.slice(IntRange(aplicationAndPidEnd + 2, afterHostname.length - 1))
  }
}
