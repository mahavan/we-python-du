from models.pizza import Pizza
from models.topping import Topping

class OrderMenu:
    def __init__(self, controller):
        self.controller = controller

    def display(self):
        print("Order Menu")
        print("Choose a pizza:")
        pizza_options = [
            {"name": "Margherita", "price": 120.0},
            {"name": "Pepperoni", "price": 150.0},
            {"name": "Hawaiian", "price": 160.0},
            {"name": "Veggie", "price": 140.0},
            {"name": "BBQ Chicken", "price": 190.0},
            {"name": "Meat Lovers", "price": 210.0},
            {"name": "Four Cheese", "price": 175.0}
        ]

        for i, pizza in enumerate(pizza_options):
            print(f"{i + 1}. {pizza['name']} - {pizza['price']} CZK")

        choice = int(input("Select a pizza by number: "))
        selected_pizza = pizza_options[choice - 1]

        size = input("Enter size (small/medium/large): ")
        price = selected_pizza["price"]
        pizza = Pizza(selected_pizza["name"], size, price)

        print("Choose toppings:")
        topping_options = [
            {"name": "Mushrooms", "price": 25.0},
            {"name": "Onions", "price": 15.0},
            {"name": "Olives", "price": 20.0},
            {"name": "Pepperoni", "price": 35.0},
            {"name": "Extra Cheese", "price": 30.0},
            {"name": "Bacon", "price": 40.0},
            {"name": "Pineapple", "price": 25.0}
        ]

        for i, topping in enumerate(topping_options):
            print(f"{i + 1}. {topping['name']} - {topping['price']} CZK")

        while True:
            topping_choice = input("Select a topping by number (or 'done'): ")
            if topping_choice == "done":
                break
            topping_choice = int(topping_choice)
            selected_topping = topping_options[topping_choice - 1]
            topping = Topping(selected_topping["name"], selected_topping["price"])
            pizza.add_topping(topping)

        self.controller.create_order(pizza)
        print("Pizza added to order.")
