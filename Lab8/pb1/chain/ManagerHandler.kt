package chain

class ManagerHandler(var next1: Handler? = null, var next2: Handler? = null) : Handler {
  override fun handleRequest(forwardDirection: String, messageToBeProcessed: String) {
    TODO()
  }
}
