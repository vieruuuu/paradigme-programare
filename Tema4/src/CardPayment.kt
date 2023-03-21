class CardPayment(private val bankAccount: BankAccount) : PaymentMethod {
  override public fun pay(fee: Double): Boolean {
    return this.bankAccount.updateAmount(fee)
  }
}
