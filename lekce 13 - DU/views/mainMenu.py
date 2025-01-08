class MainMenu:
    def __init__(self, controller):
        self.controller = controller

    def display(self):
        while True:
            print("Main Menu")
            print("1. Order Pizza")
            print("2. Admin")
            print("3. View Current Order")
            print("4. Make Payment")
            print("5. Cancel Current Order")
            print("6. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                self.order_pizza()
            elif choice == "2":
                self.admin_access()
            elif choice == "3":
                self.view_current_order()
            elif choice == "4":
                self.make_payment()
            elif choice == "5":
                self.cancel_current_order()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Try again.")

    def order_pizza(self):
        from views.orderMenu import OrderMenu
        order_menu = OrderMenu(self.controller)
        order_menu.display()

    def admin_access(self):
        from models.auth import Auth
        from utils.parser import OrderParser
        auth = Auth()
        password = input("Enter admin password: ")
        if auth.authenticate(password):
            print("Loading Orders from File...")
            loaded_orders = OrderParser.read_orders_from_file()
            for order in loaded_orders:
                self.controller.sales.record_sale(order)
            print("Orders loaded successfully.")
            print("Loaded Orders:")
            print(self.controller.sales.detailed_sales())
        else:
            print("Access Denied: Incorrect password.")

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

    def cancel_current_order(self):
        self.controller.cancel_order()
        print("The current order has been canceled.")
