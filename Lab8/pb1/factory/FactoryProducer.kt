package factory

class FactoryProducer {
  fun getFactory(choice: String): AbstractFactory {
    when (choice) {
      "elite" -> return EliteFactory()
      "happy-worker" -> return HappyWorkerFactory()
    }

    throw RuntimeException("Invalid factory choice $choice")
  }
}
