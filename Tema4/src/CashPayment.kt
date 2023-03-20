class CashPayment(private var availableAmount: Double) : PaymentMethod {

  override public fun pay(fee: Double): Boolean {
    val enoughMoney = this.availableAmount >= fee

    if (enoughMoney) {
      this.availableAmount -= fee
    }

    return enoughMoney
  }
}
