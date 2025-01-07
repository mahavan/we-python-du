class MainMenu:
    def __init__(self, controller):
        self.controller = controller

    def display(self):
        while True:
            print("Main Menu")
            print("1. Order Pizza")
            print("2. View Sales")
            print("3. View Current Order")
            print("4. Make Payment")
            print("5. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                self.order_pizza()
            elif choice == "2":
                self.view_sales()
            elif choice == "3":
                self.view_current_order()
            elif choice == "4":
                self.make_payment()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Try again.")

    def order_pizza(self):
        from views.orderMenu import OrderMenu
        order_menu = OrderMenu(self.controller)
        order_menu.display()

    def view_sales(self):
        print("Sales Report:")
        print(self.controller.sales.detailed_sales())

    def view_current_order(self):
        print("Current Order:")
        print(self.controller.order.list_order())

    def make_payment(self):
        if not self.controller.order.pizzas:
            print("No items in the order to pay for.")
            return
        print("Select Payment Method:")
        print("1. Credit Card")
        print("2. Cash")
        method = input("Enter choice: ")
        if method == "1":
            self.controller.process_payment("card")
        elif method == "2":
            self.controller.process_payment("cash")
        else:
            print("Invalid payment method.")