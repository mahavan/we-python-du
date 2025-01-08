from views.mainMenu import MainMenu
from models.order import Order
from models.sales import Sales
from models.payment import Payment, CreditCardPayment, CashPayment

class MainController:
    def __init__(self):
        self.order = Order()
        self.sales = Sales()

    def run(self):
        menu = MainMenu(self)
        menu.display()

    def create_order(self, pizza):
        self.order.add_pizza(pizza)

    def process_payment(self, method):
        payment = Payment(CreditCardPayment() if method == "card" else CashPayment())
        payment.process_payment(self.order.total_price())
        self.order.set_payment_method("Credit Card" if method == "card" else "Cash")
        self.sales.record_sale(self.order)
        self.order = Order()  # Reset order after payment

    def cancel_order(self):
        self.order = Order()  # Reset the current order