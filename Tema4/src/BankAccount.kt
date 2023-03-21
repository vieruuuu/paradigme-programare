import java.time.*

class BankAccount(
    private var availableAmount: Double,
    private val cardNumber: String,
    private val expirationDate: LocalDate,
    private val cvvCode: Int,
    private val userName: String
) {

  public fun updateAmount(value: Double): Boolean {
    val enoughMoney = this.availableAmount >= value

    if (enoughMoney) {
      this.availableAmount -= value
    }

    return enoughMoney
  }
}
