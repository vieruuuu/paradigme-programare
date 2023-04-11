package factory

import chain.Handler
import chain.HappyWorkerHandler

class HappyWorkerFactory : AbstractFactory() {
  override fun getHandler(handler: String): Handler {
    when (handler) {
      "happy-worker" -> return HappyWorkerHandler()
    }

    throw RuntimeException("Invalid handler $handler")
  }
}
