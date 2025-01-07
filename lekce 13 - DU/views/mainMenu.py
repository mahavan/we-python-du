class MainMenu:
    def __init__(self, controller):
        self.controller = controller

    def display(self):
        while True:
            print("Main Menu")
            print("1. Order Pizza")
            print("2. View Sales")
            print("3. View Current Order")
            print("4. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                self.order_pizza()
            elif choice == "2":
                self.view_sales()
            elif choice == "3":
                self.view_current_order()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Try again.")

    def order_pizza(self):
        from views.orderMenu import OrderMenu
        order_menu = OrderMenu(self.controller)
        order_menu.display()

    def view_sales(self):
        print(f"Total sales: {self.controller.sales.total_sales()} CZK")

    def view_current_order(self):
        print("Current Order:")
        print(self.controller.order.list_order())

