class Order:
    def __init__(self):
        self.pizzas = []
        self.payment_method = None

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def total_price(self):
        return sum(pizza.price for pizza in self.pizzas)

    def set_payment_method(self, method):
        self.payment_method = method

    def get_payment_method(self):
        return self.payment_method or "Unknown"

    def list_order(self):
        if not self.pizzas:
            return "No pizzas in the current order."
        result = []
        for i, pizza in enumerate(self.pizzas, start=1):
            toppings = ", ".join([topping.name for topping in pizza.toppings]) or "No toppings"
            result.append(f"{i}. {pizza.size.capitalize()} {pizza.name} - {pizza.price} CZK (Toppings: {toppings})")
        return "\n".join(result)