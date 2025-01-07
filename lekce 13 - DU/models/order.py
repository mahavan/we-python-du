class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def total_price(self):
        return sum(pizza.price for pizza in self.pizzas)

    def list_order(self):
        if not self.pizzas:
            return "No pizzas in the current order."
        result = []
        for i, pizza in enumerate(self.pizzas, start=1):
            toppings = ", ".join([topping.name for topping in pizza.toppings]) or "No toppings"
            result.append(f"{i}. {pizza.size.capitalize()} {pizza.name} - {pizza.price} CZK (Toppings: {toppings})")
        return "\n".join(result)
