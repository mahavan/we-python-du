class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)

class CreditCardPayment:
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class CashPayment:
    def pay(self, amount):
        print(f"Paid {amount} in Cash.")
