class MainMenu:
    def __init__(self, controller):
        self.controller = controller

    def display(self):
        while True:
            print("Main Menu")
            print("1. Order Pizza")
            print("2. View Sales")
            print("3. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                self.order_pizza()
            elif choice == "2":
                self.view_sales()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Try again.")

    def order_pizza(self):
        name = input("Enter pizza name: ")
        size = input("Enter size (small/medium/large): ")
        price = float(input("Enter base price: "))
        pizza = Pizza(name, size, price)

        while True:
            topping_name = input("Enter topping name (or 'done'): ")
            if topping_name == "done":
                break
            topping_price = float(input("Enter topping price: "))
            topping = Topping(topping_name, topping_price)
            pizza.add_topping(topping)

        self.controller.create_order(pizza)
        print("Pizza added to order.")

    def view_sales(self):
        print(f"Total sales: {self.controller.sales.total_sales()}")
