import java.time.*

fun main() {
  val contuMeu = BankAccount(50.0, "1234 5678 1111 2222", LocalDate.now(), 333, "VIERU SE STIE")

  val plataMega = CardPayment(contuMeu)

  println("oare a mers plata mega 1 ?: " + plataMega.pay(10.0))
  println("oare a mers plata mega 2 ?: " + plataMega.pay(60.0))

  val plataSuperbet = CashPayment(100.0)

  println("oare a mers plata superbet ?: " + plataSuperbet.pay(100.0))
}
