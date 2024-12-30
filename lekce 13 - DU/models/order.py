class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def total_price(self):
        return sum(pizza.price for pizza in self.pizzas)
