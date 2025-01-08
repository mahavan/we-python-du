import json
from models.order import Order
from models.pizza import Pizza
from models.topping import Topping


class OrderParser:
    @staticmethod
    def write_orders_to_file(orders, filename="orders.json"):
        with open(filename, "w") as file:
            json.dump([OrderParser.order_to_dict(order) for order in orders], file, indent=4)

    @staticmethod
    def read_orders_from_file(filename="orders.json"):
        try:
            with open(filename, "r") as file:
                orders_data = json.load(file)
                return [OrderParser.dict_to_order(data) for data in orders_data]
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return []

    @staticmethod
    def order_to_dict(order):
        return {
            "pizzas": [
                {
                    "name": pizza.name,
                    "size": pizza.size,
                    "price": pizza.price,
                    "toppings": [{"name": topping.name, "price": topping.price} for topping in pizza.toppings]
                } for pizza in order.pizzas
            ],
            "payment_method": order.get_payment_method()
        }

    @staticmethod
    def dict_to_order(data):
        order = Order()
        for pizza_data in data["pizzas"]:
            pizza = Pizza(
                pizza_data["name"],
                pizza_data["size"],
                pizza_data["price"]
            )
            pizza.toppings = [Topping(t["name"], t["price"]) for t in pizza_data["toppings"]]
            order.add_pizza(pizza)
        order.set_payment_method(data.get("payment_method", "Unknown"))
        return order
